# 💀 PhantomMailer

**PhantomMailer** is a web-based email spoofing tool built using Flask and Postfix. Inspired by [emkei.cz](https://emkei.cz/), it is designed for ethical red teaming, penetration testing, and SPF/DKIM/DMARC testing in secure lab environments.

---

## 🚨 Disclaimer

> ⚠️ This tool is for **educational and authorized use only**. Sending spoofed emails without permission is illegal. Use responsibly in test environments or with written consent from target organizations.

---

## 🎯 Features

- 🔥 Send spoofed emails from any sender address
- 🌐 Web interface (like Emkei.cz)
- 📨 Send messages using your local Postfix SMTP server (no authentication)
- 🧪 Ideal for testing spam filters, SPF, DKIM, and DMARC policies
- 💻 100% local — no data leaves your machine

---

## 📸 Screenshot

*(Insert a screenshot of the running tool here if desired)*

---

## 🛠️ Requirements

- Python 3.x
- Flask
- Postfix (local SMTP server)

---

## ⚙️ Installation & Setup

### 🔧 1. Install Postfix (Linux)

```bash
sudo apt update
sudo apt install postfix -y
```

During setup:
- Choose **Internet Site**
- Leave the system mail name as default or enter `localhost`

Edit Postfix config:

```bash
sudo nano /etc/postfix/main.cf
```

Update these lines (or add if missing):

```conf
myhostname = kali.localdomain
inet_interfaces = 127.0.0.1
mynetworks = 127.0.0.0/8 [::1]/128
smtpd_recipient_restrictions = permit_mynetworks, reject_unauth_destination
smtpd_relay_restrictions = permit_mynetworks, permit_sasl_authenticated, defer_unauth_destination
```

Then restart Postfix:

```bash
sudo postfix check
sudo systemctl restart postfix
```

---

### 🐍 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 🚀 3. Start the Flask App

```bash
python app.py
```

Visit the app at: [http://localhost:5000](http://localhost:5000)

---

## 💬 Example Usage

| Field         | Value                         |
|---------------|-------------------------------|
| From Name     | PayPal Security               |
| From Email    | support@paypal.com            |
| To Email      | you@example.com               |
| SMTP Server   | localhost                     |
| SMTP Port     | 25                            |

> 🛑 Note: Emails will be silently dropped by Gmail/Outlook unless SPF/DKIM/DMARC conditions are satisfied.

---

## 📬 Recommended Test Targets

- ✅ [ProtonMail](https://protonmail.com)
- ✅ [Mailtrap.io](https://mailtrap.io)
- ✅ [Yandex Mail](https://mail.yandex.com)
- ❌ Outlook/Gmail block spoofed messages without valid auth & DNS

---

## 🧪 Advanced Testing

To send spoofed emails to Gmail/Outlook:
- Buy a test domain (e.g., `testspoof.xyz`)
- Configure SPF/DKIM/DMARC in DNS
- Use `From: test@testspoof.xyz` in this tool

---

## 📦 Folder Structure

```
phantommailer/
├── app.py
├── spoof_mailer.py
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
```

---

## 📄 License

This tool is released under the [MIT License](LICENSE) for **ethical use only**.

---

## 👨‍💻 Author

Created by **Rushi Soalnki**  
For ethical red team simulation, email filtering evaluation, and cybersecurity education.

---
