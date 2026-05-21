import smtplib
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Gmail details
sender_email = "palanivelvijian@gmail.com"
receiver_email = "rayeesaiffath@gmail.com"
app_password = "hkbt yirl pesn lxci"

# ZIP file path
file_path = r"C:\Users\C2C.ITPG21.000\Desktop\vac.zip"

# Set sending time (24-hour format)
send_time = "14:38"

print("Program started... Waiting for scheduled time.")

while True:
    current_time = time.strftime("%H:%M")

    if current_time == send_time:

        # Create email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Email with ZIP File"

        # Email body
        body = "Hello! ZIP file is attached with this email."
        message.attach(MIMEText(body, "plain"))

        # Attach ZIP file
        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "zip")
            part.set_payload(attachment.read())

        # Encode file
        encoders.encode_base64(part)

        # Get file name
        filename = os.path.basename(file_path)

        # Add header
        part.add_header(
            "Content-Disposition",
            f'attachment; filename="{filename}"'
        )

        # Attach file
        message.attach(part)

        try:
            # Connect Gmail SMTP
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            # Login
            server.login(sender_email, app_password)

            # Send email
            server.send_message(message)

            print("Email with ZIP file sent successfully!")

            # Close server
            server.quit()

            break

        except Exception as e:
            print("Error:", e)

    # Check every 30 seconds
    time.sleep(30)
