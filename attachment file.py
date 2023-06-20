import os
import smtplib
from email.message import EmailMessage

email_id = 'janaranjanni.venkatesan@isteer.com'
email_password = "byxdaebckqugidrr"

recipient_list = ['dhaya1245@gmail.com', 'janaranjani450@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Welcome to isteer'
msg['From'] = email_id
msg['To'] = recipient_list
msg.set_content('you are log in successfully')

for each_file in os.listdir():
    if each_file == 'attachment file.py':
        continue
    with open(each_file, 'rb') as f:
        file_data = f.read()
        file_name = f.name



with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_id, email_password)
    smtp.send_message(msg)