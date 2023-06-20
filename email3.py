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

attachment_path = r"C:\Users\janaranjani.venkates\Desktop\Django\Project2\isteerimage.png"
attachment_name = "isteer.png"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

with open(attachment_path, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={attachment_name}",
    )
    message.attach(part)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, email_password)
    server.send_message(message)
