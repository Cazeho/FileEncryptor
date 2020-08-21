import os
import smtplib
from email.message import EmailMessage
EMAIL_ADDRESS='------@gmail.com'#os.environ.get('EMAIL_USER')
EMAIL_PASSWORD='-------'#os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    subject="hhhh"
    body="hello"

    msg=f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS,'------@googlemail.com',msg)
