from fpdf import FPDF
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# =========================
# Set credentials directly
# =========================
from_email = "ajaythakur96738@gmail.com"      # your Gmail
password = " xbpe bbbq inzn qrov"  # Gmail App Password
to_emails = ["dkumar@watermarkinsights.com", "ajaythakur96738@gmail.com"]  # add your own to receive

# =========================
# PDF Generate Section
# =========================
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)

today = datetime.date.today()
pdf.cell(0, 10, f"Learning Notes till {today}", ln=True, align="C")
pdf.ln(10)
pdf.set_font("Arial", "", 12)

notes = f"""
=== 1. [Date: 2025-09-18] WSL + VS Code + DevOps Setup ===
- Enabled WSL and installed VS Code
- Learned interlinking VS Code with WSL

=== 2. [Date: 2025-09-19] RingCentral, Internet & Notes Options ===
- Checked system logs, router lights, notebook vs computer for notes

=== 3. [Date: 2025-09-20] Jenkins Installation & Node Practice ===
- Installed Jenkins on WSL
- Learned npm install, node_modules, package.json basics

=== 4. [Date: 2025-09-23] Saving & Editing Notes, VS Code Commands ===
- Saved files in VS Code
- Learned basic file navigation and editing

=== 5. [Date: 2025-09-25 to 2025-09-27] Python + Jenkins + Poll SCM ===
- Learned Poll SCM trigger in Jenkins
- Python script integration with Jenkins pipeline
- GitHub push/pull commands
- Python script manual testing: python3 send_pipeline_notes.py
- Jenkins console output check
- Poll SCM cron: H/5 * * * *

=== 6. Key Learnings ===
- Jenkins + GitHub integration
- Poll SCM trigger & cron schedule
- Running Python scripts from Jenkins pipeline
- Manual testing of scripts in terminal
- GitHub commit/push basics
- GitHub Actions email notification difference from Jenkins
"""

pdf.multi_cell(0, 8, notes)
pdf_file = f"Full_Learning_Notes_till_{today}.pdf"
pdf.output(pdf_file)
print(f"✅ PDF generated successfully: {pdf_file}")

# =========================
# Email Section
# =========================
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = ", ".join(to_emails)
msg['Subject'] = f"Learning Notes till {today}"
msg.attach(MIMEText(f"Hi friends,\n\nAttached is the full DevOps & Jenkins learning notes till {today}.\n\n- Ajay", 'plain'))

with open(pdf_file, "rb") as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={pdf_file}')
    msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_email, password)
server.sendmail(from_email, to_emails, msg.as_string())
server.quit()

print(f"✅ Email sent successfully to {to_emails}!")

