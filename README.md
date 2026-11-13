# 🛡️ CyberShield Analyzer

**A Web-Based Website Security Analysis Tool**

CyberShield Analyzer is a Flask-based web application designed to help users assess basic website security indicators by analyzing a target URL and generating a structured security report.

The tool collects website and domain information, checks important security configurations, and presents the results through an interactive dashboard with a downloadable PDF report.

🔗 **Live Demo:** https://cybershieldanalyzer.onrender.com

---

## ✨ Features

- **URL Analysis:** Accepts a target website URL and performs security-related checks.
- **Security Headers Inspection:** Checks for important HTTP security headers and identifies missing configurations.
- **HTTPS Assessment:** Examines HTTPS usage and available SSL-related information.
- **Domain & DNS Information:** Retrieves domain-related information, including DNS records and IP details.
- **Server Information:** Collects available server and response metadata.
- **Security Risk Assessment:** Calculates an indicative risk score based on the collected findings.
- **Protection Level:** Presents an overview of the website's observed security configuration.
- **PDF Report Generation:** Generates a downloadable report containing the analysis results.
- **Interactive Interface:** Provides a clean dashboard with animated visual elements and loading feedback.

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Flask | Backend web framework |
| HTML5 | Page structure |
| CSS3 | Styling and animations |
| JavaScript | Client-side interactions |
| SQLite (if configured) | Local data storage |
| DNS / HTTP requests | Website and domain information gathering |

---

## ⚙️ How It Works

1. The user enters a website URL.
2. The application processes the submitted URL.
3. The analyzer collects available website, DNS, and server information.
4. It inspects selected security indicators, including HTTPS and HTTP security headers.
5. The collected findings are evaluated to produce an indicative security assessment.
6. The results are displayed in a structured report.
7. The user can download the report as a PDF.

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/tala-SOC/CyberShield-Security-Analyzer.git
```

### 2. Navigate to the project directory

```bash
cd CyberShield-Security-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📊 Security Assessment

CyberShield Analyzer evaluates selected security indicators to provide an overview of a website's observable security configuration.

The assessment may include:

- HTTPS availability
- SSL-related information
- HTTP security headers
- DNS and IP information
- Server response metadata
- Identified security configuration gaps

**Important:** The generated risk score is an indicative assessment based on the checks implemented in the application. It is not a comprehensive penetration test, vulnerability scan, or guarantee that a website is secure.

---

## 🖥️ Project Preview

**Live Application:**  
https://cybershieldanalyzer.onrender.com

---

## 🔐 Responsible Use

CyberShield Analyzer is intended for educational purposes and authorized security assessment.

Only analyze websites that you own or have permission to assess. The tool should be used as an initial security-awareness and configuration-checking aid, not as a replacement for professional security testing.

---

## 👩‍💻 Developer

**Tala Ammar**  
Cybersecurity Student | Secure Web Development

GitHub: https://github.com/tala-SOC

---

*Built to explore practical web security concepts and develop hands-on cybersecurity skills.*