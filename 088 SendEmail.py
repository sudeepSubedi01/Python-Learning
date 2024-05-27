import smtplib

sender = 'test1@gmail.com'
passowrd = 'test1'
receiver = 'test2@gmail.com'
subject = 'Hello World!!'
body = 'I m talking from the whole new world'
message = f"""From: Test1{sender}
To: Test2{receiver}
Subject: {subject}\n
{body}
"""
try:
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(sender, passowrd)
  print('Logged In!!!!')
  server.sendmail(sender,receiver,message)
  print('Email has been sent!!')
except smtplib.SMTPAuthenticationError:
  print("Error encountered")