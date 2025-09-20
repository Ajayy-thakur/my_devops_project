from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "DevOps Project Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, 700, "1. Created project structure with scripts and logs folders.")
    c.drawString(50, 680, "2. Wrote backup_script.py to back up log files.")
    c.drawString(50, 660, "3. Implemented logging.py to write logs.")
    c.drawString(50, 640, "4. Created analyzelogs.py to analyze log lines.")
    c.drawString(50, 620, "5. Configured smtp.py to send emails.")
    c.drawString(50, 600, "6. Implemented send_mail_with_attachment.py for emails with attachments.")

    c.drawString(50, 570, "✅ All steps completed successfully!")

    c.save()

create_pdf("project_report.pdf")
print("project_report.pdf generated successfully ✅")

