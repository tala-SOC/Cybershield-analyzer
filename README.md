# 🛡️ CyberShield Analyzer

### Web-Based Website Security Analysis Tool

CyberShield Analyzer is a Flask-based web application designed to assess website security indicators through URL analysis.

The application examines selected security configurations, gathers domain and server information, and generates a structured security report with an indicative risk assessment.

<p align="center">
  <a href="https://cybershieldanalyzer-ten.vercel.app/">
    <strong>🚀 Live Demo — Try CyberShield Analyzer</strong>
  </a>
</p>

---

## ✨ Features

- **URL Analysis:** Analyze a target website by entering its URL.
- **Security Headers Inspection:** Identify important HTTP security headers and missing configurations.
- **HTTPS Assessment:** Check HTTPS availability and collect SSL-related information.
- **DNS & IP Information:** Retrieve available domain, DNS, and IP details.
- **Server Information:** Collect server response metadata.
- **Risk Assessment:** Generate an indicative security risk score based on collected findings.
- **Protection Overview:** Present an overview of the website's observed security configuration.
- **PDF Report Generation:** Download a structured security analysis report.
- **Interactive User Interface:** Animated visual elements, loading screen, and responsive interface.

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Backend framework |
| HTML5 | Frontend structure |
| CSS3 | Styling and animations |
| JavaScript | Frontend interactions |
| Requests | HTTP communication |
| ReportLab | PDF report generation |
| Pillow | Image processing |

---

## ⚙️ How It Works

1. Enter a website URL into the analyzer.
2. Submit the URL to initiate the analysis.
3. The application collects available website and domain information.
4. Selected security indicators are inspected, including HTTPS and HTTP security headers.
5. The collected findings are evaluated to generate an indicative risk assessment.
6. A structured report is displayed with the analysis results.
7. Download the generated report as a PDF.

---

## 🚀 Run Locally

### Prerequisites

- Python 3.10 or later
- Git

### 1. Clone the repository

```bash
git clone https://github.com/tala-SOC/Cybershield-analyzer.git
```

### 2. Navigate to the project directory

```bash
cd Cybershield-analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## 🔍 Security Assessment Scope

CyberShield Analyzer focuses on selected observable website security indicators, including:

- HTTPS availability
- SSL-related information
- HTTP security headers
- DNS and IP information
- Server response metadata
- Security configuration gaps

**Disclaimer:** The risk score is an indicative assessment based on the checks implemented in the application. CyberShield Analyzer is not a comprehensive penetration-testing tool and does not guarantee that a website is secure.

---

## 🔐 Responsible Use

This project is intended for educational purposes and authorized website security assessment.

Only analyze websites that you own or have explicit permission to assess.

---

## 👩‍💻 Developer

**Tala Ammar**

Cybersecurity Student | Secure Web Development

- GitHub: [tala-SOC](https://github.com/tala-SOC)
- Project Repository: [CyberShield Analyzer](https://github.com/tala-SOC/Cybershield-analyzer)
- Live Application: [cybershieldanalyzer-ten.vercel.app](https://cybershieldanalyzer-ten.vercel.app/)

---

*Built to explore practical web security concepts through hands-on development.*
