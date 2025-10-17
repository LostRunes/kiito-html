import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
import time
import smtplib
from email.message import EmailMessage



data = pd.read_excel("participants.xlsx")


template = "certificate_template.png"


font = ImageFont.truetype("DellaRespira-Regular.ttf", 110)
text_color = (0, 0, 0)


SENDER_EMAIL = "elabs.electronics@kiit.ac.in"
SENDER_PASSWORD = "jovflocsjrjbfyhv"  
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465


os.makedirs("certificates", exist_ok=True)

def generate_certificate(name):
    cert = Image.open(template).copy()
    draw = ImageDraw.Draw(cert)
    position = (1645, 1132)
    draw.text(position, name, font=font, fill=text_color, anchor="mm")
    filename = f"certificates/{name}.png"
    cert.save(filename)
    print(f"✅ Saved: {filename}")
    return filename


with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
    server.login(SENDER_EMAIL, SENDER_PASSWORD)

    for _, row in data.iterrows():
        name = row["Name"]
        email = row["Email"]

        
        filename = generate_certificate(name)

        
        msg = EmailMessage()
        msg["Subject"] = "🤖 AI Alchemist Certificate "
        msg["From"] = SENDER_EMAIL
        msg["To"] = email
        msg.set_content(f"Hello {name},\n\nPlease Find your AI Alchemist signed certificate attached below.")

        with open(filename, "rb") as f:
            msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f"{name}.png")

        
        server.send_message(msg)
        print(f"📧 Sent certificate to {name} at {email}")

        time.sleep(2)   

