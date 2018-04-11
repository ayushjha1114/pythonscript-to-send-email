import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_user = 'test123@gmail.com'
email_send = 'test123@gmail.com'
subject = 'Python'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi There , im sending email through Python smtplib module'
msg.attach(MIMEText(body,'plain'))
text = msg.as_string()

server =smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
#server.login('test123@gmail.com','heretypeurpassword')
server.login(email_user,'heretypeurpassword')


server.sendmail('test123@gmail.com','test123@gmail.com',text)
#server.sendmail(email_user,email_send,message)

server.quit()
