import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Test Mail'
msg['From'] = 'ajaythakur96738@gmail.com'
msg['To'] = 'ajaythakur96738@gmail.com,it@superfares.com,ajaythakur82307@gmail.com,narender.kumar@superfares.com'

msg.set_content('This is a test email from Python!')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('ajaythakur96738@gmail.com', 'jznz zbxj kfic dplp')  # yaha apna 16-digit App Password dalna
    smtp.send_message(msg)

print("Email sent ✅")


