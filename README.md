This is a python project using smtplib to send reminder emails to clients.

Have you ever had to email a mass amount of emails to clients to remind them about payments and also at the same time track when you emailed each client?

This project would be a perfect demonstration of a potential solution to your problem.

This script reads an Excel file with columns such as Client's name, email address, Payment date, and Reminder Sent. 

When you run the script, it will read each Client and send a message pertaining to their name, email address, and when they need to pay 7 days before their payment date. Once it's done, it will then go into the Excel file and mark when it sent the email to each client, so you can keep track of when you sent the email to each client. It will NOT email to clients again if the Reminder Sent column is already filled.

You can link this script with a Task Scheduler on your Windows computer, to automate sending these emails everyday so that those who have not received an email yet will receive the reminder.
