from flask import Flask, render_template, request
from spoof_mailer import send_spoofed_email   # ✅ Updated import

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        from_name = request.form["from_name"]
        from_email = request.form["from_email"]
        to_email = request.form["to_email"]
        subject = request.form["subject"]
        html_content = request.form["html_content"]
        smtp_server = request.form["smtp_server"]
        smtp_port = int(request.form["smtp_port"])

        message = send_spoofed_email(from_name, from_email, to_email, subject, html_content, smtp_server, smtp_port)
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)