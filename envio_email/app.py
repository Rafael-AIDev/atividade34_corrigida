'''Programa de envio de confirmação de email, útil para sites de e-commerce'''
import smtplib # protocolo smt para envio de email
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

# classe email
class EmailAut:
    def __init__(self, destinatario, assunto, conteudo):
        self.destinatario = destinatario
        self.assunto = assunto
        self.conteudo = conteudo

    def envio(self):
        msg = MIMEMultipart()
        msg.add_header('Content-Type', 'text/html')
      
        msg['From'] = "seu_email@servidor.com"
        password = 'sua_senha'

        msg['Subject'] = self.assunto
        msg['To'] = self.destinatario
        msg.attach(MIMEText(self.conteudo, 'plain'))

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print(f'E-mail enviado para {self.destinatario}.')

if __name__ == '__main__':
    enviando = EmailAut(
        destinatario='email_destinatario@servidor.com',
        assunto = 'Assunto que deseja tratar no e-mail',
        conteudo='Texto que deseja colocar no corpo do email'
    )

    enviando.envio()