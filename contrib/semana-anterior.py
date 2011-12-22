# coding: utf-8

sender = u"Cris Monteiro <cursos@bastos.net>"
subject = u"Preparativos finais para o curso Welcome to the Django"
message = u"""
Olá {name}!

Estou entrando em contato porque as aulas do Curso Welcome to the Django começam no próximo domingo, dia 14/08.

Nesta semana nós finalizaremos os preparativos para o início do curso. Estamos montando a lista de discussão, preparando os servidores para os alunos e agendando os testes da sala de aula virtual que deverão acontecer na próxima quinta ou sexta-feira.

Em breve você receberá um email com todas as instruções para o teste da Sala de Aula Virtual e uma notificação sobre sua inclusão na lista de email da turma.

Se você tiver qualquer dúvida, estou à disposição para o que precisar.

Será um prazer ter você com a gente!

Atenciosamente,
--
Cris Monteiro
Curso Welcome to the Django
Aprenda Python e Django na Prática!
"""

if __name__ == '__main__':
    from alunos import alunos
    from libmail import Email, GmailSender

    emails = []
    for aluno in alunos:
        if aluno['status'] == u'MA':
            emails.append(Email(sender, u"{name} <{email}>".format(**aluno), subject, message.format(**aluno)))
    print len(emails)

    user, password = GmailSender.ask_credentials()
    g = GmailSender(user, password)
    g.send_mail(emails, dryrun=False)
