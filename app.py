
from flask import Flask, render_template, request, send_file
import os

from scanner import scan_website
from report_pdf import generate_pdf

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    url = request.form.get("url")
    report = scan_website(url)

    return render_template(
        "report.html",
        report=report
    )


@app.route("/download-pdf", methods=["POST"])
def download_pdf():
    url = request.form.get("url")
    report = scan_website(url)

    filename = "CyberShield_Security_Report.pdf"

    generate_pdf(report, filename)

    return send_file(
        filename,
        as_attachment=True,
        download_name=filename,
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
