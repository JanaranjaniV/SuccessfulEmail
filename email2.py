import os
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import ssl

sender_email = "janaranjani.venkatesan@isteer.com"
receiver_email = "janaranjani450@gmail.com"
email_password = "byxdaebckqugidrr"
subject = "Email with Attachment"
body = "Please find the attached text file."

attachment_path = r"C:\Users\janaranjani.venkates\Desktop\Django\Project2\static\dummy.pdf"
attachment_name = "dummy.pdf"

message = MIMEMultipart()
em = EmailMessage()
em['From'] = sender_email
em['To'] = receiver_email
em['Subject'] = subject

em.set_content(body)


message.attach(MIMEText(body, "plain"))

with open(attachment_path, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; file_name= {attachment_name}",
    )


smtp_server = "smtp.gmail.com"
smtp_port = 465

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender_email, email_password)
    smtp.sendmail(sender_email, receiver_email, em.as_string())

print("Email with attachment sent successfully.")

