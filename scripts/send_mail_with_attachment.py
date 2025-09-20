import smtplib
from email.message import EmailMessage

# 1. Email setup
SENDER = "ajaythakur96738@gmail.com"     # apna email
RECEIVER = "ajaythakur96738@gmail.com"   # jisko bhejna hai (tum khud ko test ke liye rakh lo)
APP_PASSWORD = "jznz zbxj kfic dplp"  # apna app password paste karo

# 2. Create email message
msg = EmailMessage()
msg['Subject'] = "DevOps Project Report"
msg['From'] = SENDER
msg['To'] = RECEIVER
msg.set_content("Hi,\n\nPlease find attached the project report PDF generated from Python.\n\nRegards,\nAjay")

# 3. Attach PDF
with open("final_project_report.pdf", "rb") as f:
    file_data = f.read()
    file_name = "final_project_report.pdf"
    msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

# 4. Send mail
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(SENDER, APP_PASSWORD)
    smtp.send_message(msg)

print("📧 Email with attachment sent successfully ✅")





