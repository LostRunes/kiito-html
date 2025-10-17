import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "elabs.electronics@kiit.ac.in"
SENDER_PASSWORD = "jovflocsjrjbfyhv"  
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# Recipients
TO = ["elabs.electronics@kiit.ac.in"]
CC = ["2229060@kiit.ac.in",
"2330346@kiit.ac.in", "2305798@kiit.ac.in",
"2305792@kiit.ac.in","2405338@kiit.ac.in",
"2405327@kiit.ac.in",
"2304135@kiit.ac.in",
"2330112@kiit.ac.in",
"24052032@kiit.ac.in",
"24052043@kiit.ac.in",
"24052009@kiit.ac.in",
"2305811@kiit.ac.in",
"2430205@kiit.ac.in",
"23051406@kiit.ac.in",
"23053688@kiit.ac.in",
"24155358@kiit.ac.in",
"24155359@kiit.ac.in",
"24052269@kiit.ac.in",
"2405697@kiit.ac.in",
"24052328@kiit.ac.in",
"24052277@kiit.ac.in",
"2307051@kiit.ac.in",
"23053166@kiit.ac.in",
"23053159@kiit.ac.in",
"24052042@kiit.ac.in",
"24052075@kiit.ac.in",
"2430195@kiit.ac.in",
"24051590@kiit.ac.in",
"25051991@kiit.ac.in",
"2305982@kiit.ac.in",
"25052094@kiit.ac.in",
"24156186@kiit.ac.in",
"2404170@kiit.ac.in",
"25051939@kiit.ac.in",
"24052501@kiit.ac.in",
"24052369@kiit.ac.in",
"24051224@kiit.ac.in",
"24155375@kiit.ac.in",
"25051754@kiit.ac.in",
"24155366@kiit.ac.in",
"2429051@kiit.ac.in",
"2429050@kiit.ac.in",
"2429052@kiit.ac.in",
"2429050@kiit.ac.in",
"2405987@kiit.ac.in",
"24155943@kiit.ac.in",
"2405977@kiit.ac.in",
"2405986@kiit.ac.in",
"24052401@kiit.ac.in",
"24051291@kiit.ac.in",
"2329087@kiit.ac.in",
"2330050@kiit.ac.in",
"24051351@kiit.ac.in",
"24155313@kiit.ac.in",
"24159005@kiit.ac.in",
"2405600@kiit.ac.in",
"2405327@kiit.ac.in",
"24155483@kiit.ac.in",
"22051176@kiit.ac.in",
"24051085@kiit.ac.in",
"25156090@kiit.ac.in",
"24051210@kiit.ac.in",
"2407040@kiit.ac.in",
"2505237@kiit.ac.in",
"2530034@kiit.ac.in",
"25156027@kiit.ac.in",
"25156040@kiit.ac.in",
"24052392@kiit.ac.in",
"24052435@kiit.ac.in",
"24052357@kiit.ac.in",
"23053433@kiit.ac.in",
"23053475@kiit.ac.in",
"24052497@kiit.ac.in",
"2527033@kiit.ac.in",
"2505297@kiit.ac.in",
"2527029@kiit.ac.in",
"25052066@kiit.ac.in","2430256@kiit.ac.in"] #"2229060@kiit.ac.in",
#"2330346@kiit.ac.in",
#"2305792@kiit.ac.in", "2305798@kiit.ac.in",
BCC = [
"2430256@kiit.ac.in"
]


# Load cleaned HTML
with open("hostelperm.html", "r", encoding="utf-8") as f:
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
        recipients = TO + CC + BCC  # ✅ BCC is included here but not shown in headers
        server.send_message(msg, to_addrs=recipients)
    print("📧 Mail sent successfully!")
except Exception as e:
    print("❌ Error sending mail:", e)
