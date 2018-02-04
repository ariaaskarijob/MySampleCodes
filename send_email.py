#how to send an email with attachment, and a subject line, using python!

#importing the right libraries for sending email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#Email,passowrd,details
email_user = 'Your Email'
email_password = 'Your Password'
email_send = 'The Receiver Email'

#Your Custome Subject line
subject = 'Ice Cream Next Week?'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

#Your body of the email
body = 'You can write anything here, just like an email.'
msg.attach(MIMEText(body,'plain'))

#Attach-file, making sure the code runs within the same folder.
filename='2.jpg'
attachment  =open(filename,'rb')

#encoding and standard steps
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)
msg.attach(part)
text3 = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)

#where the actual email gets send, and quits after
server.sendmail(email_user,email_send,text3)
server.quit()

