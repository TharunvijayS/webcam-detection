import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = 'tbtx dstm ioko bvrd'
SENDER = "tharunapp8@gmail.com"
RECEIVER = "tharunapp8@gmail.com"

def send_email(image_path):
    print("send email function started")
    email_message = EmailMessage()
    email_message['Subject'] = "New Customer Showed UP!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, 'rb') as file:
        content = file.read()

    image_type = imghdr.what(None, content)
    email_message.add_attachment(content, maintype='image', subtype=image_type)

    # Use port 587 for TLS/STARTTLS
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send email function ended")

if __name__ == '__main__':
    send_email(image_path='images/21.png')
