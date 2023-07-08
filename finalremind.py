import datetime
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Read the Excel file using Pandas
df = pd.read_excel('residents.xlsx')

# Iterate over each row in the DataFrame and check if it's time to send the reminder
for index, row in df.iterrows():
    name = row['Name']
    email = row['Email']
    payment_date = row['Payment Date']
    reminder_date = payment_date - datetime.timedelta(days=7)  # Calculate the reminder date

    # Check if it's time to send the reminder
    if reminder_date.date() == datetime.datetime.now().date():
        # Check if the resident has already received a reminder
        if pd.isna(row['Reminder Sent']):
            # Construct the email message
            message = MIMEMultipart()
            message['From'] = 'your_email@example.com'
            message['To'] = email
            message['Subject'] = 'Payment Reminder'
            body = f"Dear {name},\n\nThis is a reminder that your payment is due on {payment_date}.\nPlease make the payment as soon as possible.\n\nThank you.\nYour Property Management Team"
            message.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login('andrewvang99@gmail.com', 'hbmlcrdrvsgulxuh')
                server.send_message(message)
                print("Email Sent Successfully!")

            # Update the 'Reminder Sent' column to mark the reminder as sent
            df.loc[index, 'Reminder Sent'] = datetime.datetime.now().date()

# Save the updated DataFrame to the Excel file
df.to_excel('residents.xlsx', index=False)
