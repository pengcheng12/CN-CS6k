from smtplib import *

#  define server and SSL port
serverName = 'smtp.gmail.com'
serverPort = 465

#  define username and password
userName = 'p.holoubek92@gmail.com'
userPass = 'password'

recipient = 'pholoubek@yahoo.com'

#  define header
header ='\r\n'.join(["From: " + userName,
        "Subject: Hi, hello My Love",
        "To: " + recipient,
        "MIME-Version: 1.0",
        "Content-Type: text/html"])

#  message to be send
msg = 'Hi\nHello How, are you?\nI hope good.\n'

smtpSSL = SMTP_SSL(serverName, serverPort)
smtpSSL.login(userName, userPass)
smtpSSL.sendmail(userName, recipient, header + '\r\n\r\n' + msg)
smtpSSL.quit()


