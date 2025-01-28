import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

def send_email(from_contact, to_contact, subject, content):
    mail = MIMEText(content)
    mail['Subject'] = subject
    mail['From'] = from_contact
    mail['To'] = to_contact
    service = smtplib.SMTP('localhost')
    service.sendmail(from_contact, [to_contact], mail.as_string())
    service.quit()
    
if __name__ == "__main__":
    ME = os.getenv('ME')
    TO = os.getenv('TO')
    send_email(ME, TO, 'An awesome message', 'Hello world !')
