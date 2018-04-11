import smtplib

#email_user = 'test123@gmail.com'
#email_send = 'test123@gmail.com'

server =smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('test123@gmail.com','typeurpasswordhere')
#server.login(email_user,'heretypeurpassword')

message = 'Hi There , im sending email through Python smtplib module'

server.sendmail('test123@gmail.com','test123@gmail.com',message)
#server.sendmail(email_user,email_send,message)

server.quit()
