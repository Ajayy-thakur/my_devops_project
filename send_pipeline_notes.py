import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ---------------------------
# CONFIGURATION
# ---------------------------
sender_email = "ajaythakur96738@gmail.com"       # Apna Gmail
receiver_email = "dkumar@watermarkinsights.com,ajaythakur82307@gmail.com"  # Multiple receivers
password = "iemt dtym krzk jyho"                  # Gmail App Password

subject = "DevOps Pipeline Notes ✅"

# ---------------------------
# PIPELINE NOTES CONTENT
# ---------------------------
body = """
Hi Team,

Here are the detailed notes for our DevOps Jenkins pipeline:

Project: my_devops_project
Pipeline: Jenkins Declarative Pipeline
Purpose: Fully automated CI/CD workflow for artifact generation, deployment, testing, and notifications

Stages:

1. Build Stage
   - Command: echo "Hello DevOps Engineer 🚀" > report.txt
   - Purpose: Generate artifact (report.txt)
   - Real-Life Use: Software compile / script execution

2. Archive Stage
   - Command: archiveArtifacts artifacts: 'report.txt', fingerprint: true
   - Purpose: Store artifact safely
   - Real-Life Use: Backup of every build

3. Deploy Stage
   - Commands:
       mkdir -p deploy
       cp report.txt deploy/
   - Purpose: Copy artifact to deploy folder
   - Real-Life Use: Deploy to staging/production server

4. Test Stage
   - Commands:
       echo "Running tests..."
       cat deploy/report.txt
   - Purpose: Verify deployed artifact
   - Real-Life Use: Automated testing

5. Post Section (Notifications)
   - Commands (placeholders):
       slackSend channel: '#devops', message: "Build Success ✅"
       mail to: 'ajay@example.com', subject: 'Build Success', body: 'Pipeline ran successfully ✅'
   - Purpose: Notify team about build success/failure

Terminal Verification:
cd /var/lib/jenkins/workspace/DevOps-Practice25/deploy/
ls
cat report.txt

Expected Output:
report.txt
Hello DevOps Engineer 🚀

Flow:
GitHub Push → Jenkins Pipeline → Build → Archive → Deploy → Test → Notifications (Slack/Email)

Notes: Pipeline fully automated, ready for practice and real-life CI/CD workflow.
"""

# ---------------------------
# EMAIL CREATION
# ---------------------------
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# ---------------------------
# SEND EMAIL
# ---------------------------
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email.split(','), message.as_string())
    server.quit()
    print("✅ Notes successfully sent via email!")
except Exception as e:
    print("❌ Failed to send email.")
    print(e)

