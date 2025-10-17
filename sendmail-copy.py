import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "elabs.electronics@kiit.ac.in"
SENDER_PASSWORD = "jovflocsjrjbfyhv"  
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# Recipients
TO = ["elabs.electronics@kiit.ac.in"]
CC = ["2229060@kiit.ac.in",
"2330346@kiit.ac.in", "2430256@kiit.ac.in",
"2305792@kiit.ac.in","2405295@kiit.ac.in","2305798@kiit.ac.in",
] #"2229060@kiit.ac.in",
#"2330346@kiit.ac.in",
#"2305792@kiit.ac.in"
BCC = [
"btech.2023@kiit.ac.in","btech.2024@kiit.ac.in","btech.2025@kiit.ac.in",
"btech.2022@kiit.ac.in"
"a1.2023@kiit.ac.in","a2.2023@kiit.ac.in","a3.2023@kiit.ac.in","a4.2023@kiit.ac.in","a5.2023@kiit.ac.in","a6.2023@kiit.ac.in","a7.2023@kiit.ac.in","a8.2023@kiit.ac.in","a9.2023@kiit.ac.in","a10.2023@kiit.ac.in",
"a11.2023@kiit.ac.in","a12.2023@kiit.ac.in","a13.2023@kiit.ac.in","a14.2023@kiit.ac.in","a15.2023@kiit.ac.in","a16.2023@kiit.ac.in","a17.2023@kiit.ac.in","a18.2023@kiit.ac.in","a19.2023@kiit.ac.in","a20.2023@kiit.ac.in",
"a21.2023@kiit.ac.in","a22.2023@kiit.ac.in","a23.2023@kiit.ac.in","a24.2023@kiit.ac.in","a25.2023@kiit.ac.in","a26.2023@kiit.ac.in","a27.2023@kiit.ac.in","a28.2023@kiit.ac.in","a29.2023@kiit.ac.in","a30.2023@kiit.ac.in",
"a31.2023@kiit.ac.in","a32.2023@kiit.ac.in","a33.2023@kiit.ac.in","a34.2023@kiit.ac.in","a35.2023@kiit.ac.in","a36.2023@kiit.ac.in","a37.2023@kiit.ac.in","a38.2023@kiit.ac.in","a39.2023@kiit.ac.in","a40.2023@kiit.ac.in",
"b1.2023@kiit.ac.in","b2.2023@kiit.ac.in","b3.2023@kiit.ac.in","b4.2023@kiit.ac.in","b5.2023@kiit.ac.in","b6.2023@kiit.ac.in","b7.2023@kiit.ac.in","b8.2023@kiit.ac.in","b9.2023@kiit.ac.in","b10.2023@kiit.ac.in",
"b11.2023@kiit.ac.in","b12.2023@kiit.ac.in","b13.2023@kiit.ac.in","b14.2023@kiit.ac.in","b15.2023@kiit.ac.in","b16.2023@kiit.ac.in","b17.2023@kiit.ac.in","b18.2023@kiit.ac.in","b19.2023@kiit.ac.in","b20.2023@kiit.ac.in",
"b21.2023@kiit.ac.in","b22.2023@kiit.ac.in","b23.2023@kiit.ac.in","b24.2023@kiit.ac.in","b25.2023@kiit.ac.in","b26.2023@kiit.ac.in","b27.2023@kiit.ac.in","b28.2023@kiit.ac.in","b29.2023@kiit.ac.in","b30.2023@kiit.ac.in",
"b31.2023@kiit.ac.in","b32.2023@kiit.ac.in","b33.2023@kiit.ac.in","b34.2023@kiit.ac.in","b35.2023@kiit.ac.in","b36.2023@kiit.ac.in","b37.2023@kiit.ac.in","b38.2023@kiit.ac.in","b39.2023@kiit.ac.in","b40.2023@kiit.ac.in",
"a1.2024@kiit.ac.in","a2.2024@kiit.ac.in","a3.2024@kiit.ac.in","a4.2024@kiit.ac.in","a5.2024@kiit.ac.in","a6.2024@kiit.ac.in","a7.2024@kiit.ac.in","a8.2024@kiit.ac.in","a9.2024@kiit.ac.in","a10.2024@kiit.ac.in",
"a11.2024@kiit.ac.in","a12.2024@kiit.ac.in","a13.2024@kiit.ac.in","a14.2024@kiit.ac.in","a15.2024@kiit.ac.in","a16.2024@kiit.ac.in","a17.2024@kiit.ac.in","a18.2024@kiit.ac.in","a19.2024@kiit.ac.in","a20.2024@kiit.ac.in",
"a21.2024@kiit.ac.in","a22.2024@kiit.ac.in","a23.2024@kiit.ac.in","a24.2024@kiit.ac.in","a25.2024@kiit.ac.in","a26.2024@kiit.ac.in","a27.2024@kiit.ac.in","a28.2024@kiit.ac.in","a29.2024@kiit.ac.in","a30.2024@kiit.ac.in",
"a31.2024@kiit.ac.in","a32.2024@kiit.ac.in","a33.2024@kiit.ac.in","a34.2024@kiit.ac.in","a35.2024@kiit.ac.in","a36.2024@kiit.ac.in","a37.2024@kiit.ac.in","a38.2024@kiit.ac.in","a39.2024@kiit.ac.in","a40.2024@kiit.ac.in",
"b1.2024@kiit.ac.in","b2.2024@kiit.ac.in","b3.2024@kiit.ac.in","b4.2024@kiit.ac.in","b5.2024@kiit.ac.in","b6.2024@kiit.ac.in","b7.2024@kiit.ac.in","b8.2024@kiit.ac.in","b9.2024@kiit.ac.in","b10.2024@kiit.ac.in",
"b11.2024@kiit.ac.in","b12.2024@kiit.ac.in","b13.2024@kiit.ac.in","b14.2024@kiit.ac.in","b15.2024@kiit.ac.in","b16.2024@kiit.ac.in","b17.2024@kiit.ac.in","b18.2024@kiit.ac.in","b19.2024@kiit.ac.in","b20.2024@kiit.ac.in",
"b21.2024@kiit.ac.in","b22.2024@kiit.ac.in","b23.2024@kiit.ac.in","b24.2024@kiit.ac.in","b25.2024@kiit.ac.in","b26.2024@kiit.ac.in","b27.2024@kiit.ac.in","b28.2024@kiit.ac.in","b29.2024@kiit.ac.in","b30.2024@kiit.ac.in",
"b31.2024@kiit.ac.in","b32.2024@kiit.ac.in","b33.2024@kiit.ac.in","b34.2024@kiit.ac.in","b35.2024@kiit.ac.in","b36.2024@kiit.ac.in","b37.2024@kiit.ac.in","b38.2024@kiit.ac.in","b39.2024@kiit.ac.in","b40.2024@kiit.ac.in",
"a1.2025@kiit.ac.in","a2.2025@kiit.ac.in","a3.2025@kiit.ac.in","a4.2025@kiit.ac.in","a5.2025@kiit.ac.in","a6.2025@kiit.ac.in","a7.2025@kiit.ac.in","a8.2025@kiit.ac.in","a9.2025@kiit.ac.in","a10.2025@kiit.ac.in",
"a11.2025@kiit.ac.in","a12.2025@kiit.ac.in","a13.2025@kiit.ac.in","a14.2025@kiit.ac.in","a15.2025@kiit.ac.in","a16.2025@kiit.ac.in","a17.2025@kiit.ac.in","a18.2025@kiit.ac.in","a19.2025@kiit.ac.in","a20.2025@kiit.ac.in",
"a21.2025@kiit.ac.in","a22.2025@kiit.ac.in","a23.2025@kiit.ac.in","a24.2025@kiit.ac.in","a25.2025@kiit.ac.in","a26.2025@kiit.ac.in","a27.2025@kiit.ac.in","a28.2025@kiit.ac.in","a29.2025@kiit.ac.in","a30.2025@kiit.ac.in",
"a31.2025@kiit.ac.in","a32.2025@kiit.ac.in","a33.2025@kiit.ac.in","a34.2025@kiit.ac.in","a35.2025@kiit.ac.in","a36.2025@kiit.ac.in","a37.2025@kiit.ac.in","a38.2025@kiit.ac.in","a39.2025@kiit.ac.in","a40.2025@kiit.ac.in",
"b1.2025@kiit.ac.in","b2.2025@kiit.ac.in","b3.2025@kiit.ac.in","b4.2025@kiit.ac.in","b5.2025@kiit.ac.in","b6.2025@kiit.ac.in","b7.2025@kiit.ac.in","b8.2025@kiit.ac.in","b9.2025@kiit.ac.in","b10.2025@kiit.ac.in",
"b11.2025@kiit.ac.in","b12.2025@kiit.ac.in","b13.2025@kiit.ac.in","b14.2025@kiit.ac.in","b15.2025@kiit.ac.in","b16.2025@kiit.ac.in","b17.2025@kiit.ac.in","b18.2025@kiit.ac.in","b19.2025@kiit.ac.in","b20.2025@kiit.ac.in",
"b21.2025@kiit.ac.in","b22.2025@kiit.ac.in","b23.2025@kiit.ac.in","b24.2025@kiit.ac.in","b25.2025@kiit.ac.in","b26.2025@kiit.ac.in","b27.2025@kiit.ac.in","b28.2025@kiit.ac.in","b29.2025@kiit.ac.in","b30.2025@kiit.ac.in",
"b31.2025@kiit.ac.in","b32.2025@kiit.ac.in","b33.2025@kiit.ac.in","b34.2025@kiit.ac.in","b35.2025@kiit.ac.in","b36.2025@kiit.ac.in","b37.2025@kiit.ac.in","b38.2025@kiit.ac.in","b39.2025@kiit.ac.in","b40.2025@kiit.ac.in"
]


# Load cleaned HTML
with open("file4.html", "r", encoding="utf-8") as f:
    html_content = f.read()

msg = EmailMessage()
msg["Subject"] = "🤖 AI Alchemist"
msg["From"] = SENDER_EMAIL
msg["To"] = ", ".join(TO)
if CC:  
    msg["Cc"] = ", ".join(CC)

msg.set_content("This mail requires HTML view.")
msg.add_alternative(html_content, subtype="html")

# Send
try:
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        recipients = TO + CC + BCC  
        server.send_message(msg, to_addrs=recipients)
    print("📧 Mail sent successfully!")
except Exception as e:
    print("❌ Error sending mail:", e)
