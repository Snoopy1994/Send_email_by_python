"""
send email by html template
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message['from'] = 'sender'
message['to'] = 'receiver@gmail.com'
message['subject'] = 'This is your email title.'
body = template.substitute(name="receiver's name")
# body = template.substitute({"name":"receiver's name"})
message.attach(MIMEText(body, "html"))
message.attach(
    MIMEImage(Path("photo.png").read_bytes()))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender_email@gmail.com', 'sender_password')
    smtp.send_message(message)
    print('Email sent')
