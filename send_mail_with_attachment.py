import smtplib
from email.message import EmailMessage

EMAIL_USER = "ajaythakur96738@gmail.com"
EMAIL_PASS = "jznz zbxj kfic dplp"  # yaha apna Gmail App Password daalna

msg = EmailMessage()
msg["Subject"] = "DevOps Project Report"
msg["From"] = 'ajaythakur96738@gmail.com'
msg["To"] = 'ajaythakur82307@gmaul.com'  # apne aap ko bhej raha hai

msg.set_content("Attached is the project report PDF with all steps.")

# Attach the PDF
with open("project_report.pdf", "rb") as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_USER, EMAIL_PASS)
    smtp.send_message(msg)

print("Report sent with PDF ✅")

