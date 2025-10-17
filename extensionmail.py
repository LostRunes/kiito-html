import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "elabs.electronics@kiit.ac.in"
SENDER_PASSWORD = "jovflocsjrjbfyhv"  
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# Recipients
TO = ["kingpalace.25b@kiit.ac.in","kingpalace.25c@kiit.ac.in"]  # Example
CC = ["2229060@kiit.ac.in"]  # Example
BCC = [ "2428038@kiit.ac.in"]

# Plain text message
plain_text = """\

Kindly allow,
24051287- Soumya Ranjan Mohapatra 
2428038- Raghav Sinha 
for late time entry till 8:30 PM as
he is working for Elabs under SoEE.

-----------
Best Regards,  
Team E Labs.



---------------------------
E Labs, School of Electronics Engineering,
Kalinga Institute of Industrial Technology (Deemed to be University),
Bhubaneswar
"""

# Create the email
msg = EmailMessage()
msg["Subject"] = "Late Time extension due to society works|School of Electronics Engineering"
msg["From"] = SENDER_EMAIL
msg["To"] = ", ".join(TO)
if CC:
    msg["Cc"] = ", ".join(CC)

# Set plain text content
msg.set_content(plain_text)

# Send the email
try:
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        recipients = TO + CC + BCC  # Include BCC silently
        server.send_message(msg, to_addrs=recipients)
    print("📧 Mail sent successfully!")
except Exception as e:
    print("❌ Error sending mail:", e)
