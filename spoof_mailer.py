import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_spoofed_email(from_name, from_email, to_email, subject, html_content, smtp_server, smtp_port):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"{from_name} <{from_email}>"
    msg["To"] = to_email
    msg.attach(MIMEText(html_content, "html"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        return "[+] Spoofed email sent!"
    except Exception as e:
        return f"[-] Error: {str(e)}"
