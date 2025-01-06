# email_sender.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
SENDER_EMAIL = "frezwoan@gmail.com"
PASSWORD = "frrqkbhxfkoqmwcl"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # Use 465 for SSL

def send_email(receiver_email,name, referral_code):
    """
    Sends an HTML email to the specified receiver with personalized content.

    Args:
        receiver_email (str): Recipient's email address.
        first_name (str): Recipient's first name.
        last_name (str): Recipient's last name.
        referral_code (str): Referral code to include in the email.
    """
    # Create the referral link
    referral_link = f"https://chi.ke/signup?ref={referral_code}"

    # Email subject
    subject = "Welcome to chi.ke! Here's Your Referral Code"

    # HTML Email Body
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <style>
            /* General Styles */
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
            }}
            .email-container {{
                max-width: 600px;
                margin: 20px auto;
                background: #ffffff;
                border: 1px solid #eaeaea;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            }}

            /* Header Section */
            .email-header {{
                background: linear-gradient(135deg, #67358e, #34c759);
                color: #ffffff;
                padding: 30px 20px;
                text-align: center;
            }}
            .email-header img {{
                height: 50px;
                padding: 5px;
                margin-bottom: 10px;
            }}
            .email-header h1 {{
                margin: 0;
                font-size: 26px;
                font-weight: bold;
            }}

            /* Body Section */
            .email-body {{
                padding: 25px 20px;
            }}
            .email-body p {{
                margin: 0 0 15px;
                font-size: 16px;
                line-height: 1.6;
                color: #333333;
            }}
            .email-body .referral-link {{
                display: block;
                font-size: 16px;
                color: #67358e;
                text-decoration: none;
                word-wrap: break-word;
                margin: 20px 0;
                padding: 10px;
                background: #f4f4f9;
                border-radius: 10px;
                text-align: center;
                box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
            }}

            /* Footer Section */
            .email-footer {{
                text-align: center;
                padding: 15px;
                font-size: 12px;
                color: #888888;
                background-color: #f9f9f9;
            }}
            .green-accent {{
                color: #34c759;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <!-- Header -->
            <div class="email-header">
                <img
                    src="https://i.postimg.cc/d3M0sLyS/logo.png"
                    alt="chi.ke Logo"
                />
                <h1>Welcome to chi.ke!</h1>
            </div>

            <!-- Body -->
            <div class="email-body">
                <p>Hi <strong>{name}</strong>,</p>
                <p>
                    We’re thrilled to have you with us! Below is your unique referral link:
                </p>
                <a href="{referral_link}" class="referral-link">{referral_link}</a>

                <p>
                    Copy the link above and share it with your friends and family. Sharing your referral link helps you earn
                    <span class="green-accent">exclusive rewards</span>. Start sharing today!
                </p>
            </div>

            <!-- Footer -->
            <div class="email-footer">
                <p>
                    Thank you for being part of the
                    <strong>chi.ke</strong> community. We’re here to help you
                    climb the leaderboard!
                </p>
            </div>
        </div>
    </body>
    </html>
    """

    # Create a multipart message
    message = MIMEMultipart("alternative")
    message["From"] = SENDER_EMAIL
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the HTML content
    message.attach(MIMEText(html, "html"))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection

        # Log in to the server
        server.login(SENDER_EMAIL, PASSWORD)

        # Send the email
        server.send_message(message)

        print(f"Email sent successfully to {receiver_email}")

    except Exception as e:
        print(f"Failed to send email to {receiver_email}. Error: {e}")

    finally:
        # Terminate the SMTP session
        server.quit()
