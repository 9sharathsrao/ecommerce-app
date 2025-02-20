import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body, recipient):
    sender = "your-email@example.com"
    password = "your-email-password"  # Replace with secure env variable in production
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())

if __name__ == "__main__":
    send_alert("High CPU Usage Alert", "CPU usage exceeded 80%", "admin@example.com")