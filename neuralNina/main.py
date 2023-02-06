import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.world4you.com',25)
server.ehlo()

with open('password.txt','r') as f:
    password = f.read()

server.login('mail.mail.com', password)

msg = MIMEMultipart()
msg['from'] = 'NeuralNine'
msg['To'] = 'testmail@spam1.de'
msg['Subject'] = 'Just & test'

with open('message.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message,'plain'))
filename = 'coding.jpeg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content_Disposition",f'attachment: filename={filename}')
msg.attach(p)
text = msg.as_string()
server.sendmail('mailtesting@neuralnine.com','testmails@spam1.de',text)


