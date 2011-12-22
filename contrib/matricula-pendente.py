# coding: utf-8

sender = u"Cris Monteiro <cursos@bastos.net>"
subject = u"Matrícula pendente no curso Welcome to the Django"
message = u"""
Olá {name}!

Estou entrando em contato porque as aulas do Curso Welcome to the Django começam no próximo domingo, dia 14/08.

Nesta semana nós estamos preparando os alunos para o início do curso. Estamos montando a lista de discussão, preparando os servidores para os alunos e agendando os testes da sala de aula virtual que acontecerão na próxima sexta-feira.

Verificamos que sua matrícula ainda não foi concluída. Por isso, gostaríamos de saber se você continua interessado no curso, e se possui qualquer dúvida com relação as aulas ou com relação ao pagamento.

Para concluir a sua matrícula, basta acessar o link abaixo e você será encaminhado ao Pagseguro.

http://welcometothedjango.com.br/inscricao/{hash}/sucesso/

Aguardo seu retorno e desde já, fico à disposição para o que você precisar.

Será um prazer ter você conosco!

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
        if aluno['status'] in [u'MA']:
            continue

        emails.append(
            Email(sender, u"{name} <{email}>".format(**aluno), subject, message.format(**aluno))
        )

    user, password = GmailSender.ask_credentials()
    g = GmailSender(user, password)
    g.send_mail(emails, dryrun=True)
