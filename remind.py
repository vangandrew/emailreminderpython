import time
import datetime
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# read excel file
df = pd.read_excel('residents.xlsx')

# calculate the desired time to send email
reminder_datetime = datetime.datetime.now() + datetime.timedelta(seconds=5)

current_datetime = datetime.datetime.now()
time_difference = (reminder_datetime - current_datetime).total_seconds()
time.sleep(time_difference)

#iterate over each row
for index, row in df.iterrows():
    name = row['Name']
    email = row['Email']
    payment_date = row['Payment Date']
    reminder_date = payment_date - datetime.timedelta(days=7)

    # The email message 
    message = MIMEMultipart()
    message['From'] = 'andrewvang99@gmail.com'
    message['To'] = email
    message['Subject'] = 'Payment Reminder'
    body = f"Dear {name}, \n\nThis is a reminder about your payment on {payment_date}"
    message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP Server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('andrewvang99@gmail.com', 'hbmlcrdrvsgulxuh')
        server.send_message(message)
        print("Email sent successfully!")

