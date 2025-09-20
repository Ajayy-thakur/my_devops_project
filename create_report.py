from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "DevOps Project Report")

    c.setFont("Helvetica", 12)
    lines = [
        "Steps Completed:",
        "1. Logging script banaya (logs/aap.log)",
        "2. Backup script banaya (backup_script.py)",
        "3. Log analysis script banaya (analyzelogs.py)",
        "4. Email sending script banaya (send_mail.py)",
        "5. Gmail App Password use karke mail send successfully",
        "6. Tested sending mail to self + recipient",
        "7. Next step: Attachment ke saath mail send karna"
    ]

    y = height - 100
    for line in lines:
        c.drawString(50, y, line)
        y -= 20

    c.showPage()
    c.save()

create_pdf("project_report.pdf")
print("PDF created ✅ -> project_report.pdf")

