#Send email via SMTP
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    print(subject, body, to_email)
    # Your email credentials
    from_email = "vigneshsundaram122004@gmail.com"
    password = "qxji ijfx tgda kkkr"  # or an app-specific password

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    body = MIMEText(body)

    # Attach the email body
    msg.attach(body)

    # Connect to the SMTP server
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
            server.login(from_email, password)  # Login to your email account
            server.send_message(msg)  # Send the email
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
# send_email(
#     subject="Test Email",
#     body="Hello! This is a test email sent from Python.",
#     to_email="recipient@example.com"
# )
