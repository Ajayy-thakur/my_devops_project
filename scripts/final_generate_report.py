from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# PDF banane ka function
def create_final_report(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 50, "DevOps Automation Project Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, "Author: Ajay Thakur")
    c.drawString(50, height - 120, "Email Automation, Logs & Backup System")

    c.line(50, height - 130, 550, height - 130)

    y = height - 160
    steps = [
        "1. Backup Script: Automated log backup using shutil.copy",
        "2. Log Analyzer: Counted total log lines from logs/app.log",
        "3. Mail Sender: Sent email via Gmail SMTP using App Password",
        "4. PDF Generator: Created reports with ReportLab library",
        "5. Attachment Mail: Sent PDF report as email attachment",
    ]

    for step in steps:
        c.drawString(50, y, step)
        y -= 20

    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, 80, "✅ Project successfully executed!")
    c.drawString(50, 60, "Date: Auto-generated")

    c.save()

# Run
create_final_report("final_project_report.pdf")
print("final_project_report.pdf generated successfully ✅")

