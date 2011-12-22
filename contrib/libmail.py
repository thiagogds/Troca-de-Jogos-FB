# coding: utf-8
import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders


class Email(object):
    def __init__(self, sender, to, subject, message, attachment=None):
        """
        Usage:
        Email('henrique@bastos.net', 'cursos@bastos.net', 'Subject', 'Message.')
        Email('henrique@bastos.net', ['cursos@bastos.net', 'other@bastos.net], 'Subject', 'Message.')
        Email('henrique@bastos.net', 'cursos@bastos.net', 'Subject', 'Message.', '/path/to/file.ext')
        """
        assert isinstance(sender, basestring), "SENDER must be a string."

        if isinstance(to, (list, tuple)):
            to = COMMASPACE.join(to)
        assert isinstance(to, basestring), "TO must be a string or a list of strings."

        self._multipart = MIMEMultipart()
        self._multipart['From'] = sender
        self._multipart['To'] = to
        self._multipart['Date'] = formatdate(localtime=True)
        self._multipart['Subject'] = subject
        self._multipart.attach(MIMEText(message.encode('UTF-8')))

        if attachment:
            self.add_attachment(attachment)

    def add_attachment(self, pathfilename):
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(pathfilename, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(pathfilename))
        self._multipart.attach(part)

    @property
    def sender(self):
        return self._multipart['From']

    @property
    def to(self):
        return self._multipart['To']

    @property
    def subject(self):
        return self._multipart['Subject']

    @property
    def body(self):
        return self._multipart.as_string()


class MailSender(object):
    def __init__(self, host, port, user, password):
        self._host = host
        self._port = port
        self._user = user
        self._password = password

    def _open(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self._user, self._password)
        return server

    def send_mail(self, emails, dryrun=False):
        server = self._open()
        for email in emails:
            print "Sending mail from %s to %s ..." % (email.sender, email.to)
            if dryrun:
                print email.body
            else:
                server.sendmail(email.sender, email.to, email.body)
        # Should be mailServer.quit(), but that crashes...
        server.close()


class GmailSender(MailSender):
    def __init__(self, user, password):
        super(GmailSender, self).__init__('smtp.gmail.com', 587, user, password)

    @staticmethod
    def ask_credentials():
        from getpass import getpass
        return raw_input('Gmail user: '), getpass('Gmail password: ')


if __name__ == '__main__':
    """
    sender = u"cursos@bastos.net>"
    subject = u"Subject"
    message = u"Message content."

    emails = [
        Email(sender, u"Henrique Bastos <henrique@bastos.net>", subject, message, "file.txt"),
    ]

    user, password = GmailSender.ask_credentials()
    g = GmailSender(user, password)
    g.send_mail(emails, dryrun=True)
    """