import requests
import socket
import time
import ssl
from urllib.parse import urlparse


def normalize_url(url):
    """
    Normalize user input into a valid URL.
    Examples:
    youtube.com -> https://youtube.com
    www.youtube.com -> https://www.youtube.com
    https://youtube.com -> https://youtube.com
    http://youtube.com -> http://youtube.com
    """

    url = url.strip()

    if not url:
        raise ValueError("Please enter a website URL.")

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url


def check_ssl(domain):

    try:

        context = ssl.create_default_context()

        with socket.create_connection(
            (domain, 443),
            timeout=5
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=domain
            ) as ssock:

                cert = ssock.getpeercert()

                return {

                    "valid": True,

                    "expiry": cert.get(
                        "notAfter",
                        "Unknown"
                    )

                }

    except Exception as e:

        return {

            "valid": False,

            "error": str(e)

        }


def scan_website(url):

    report = {}

    try:

        # Normalize the user's input
        url = normalize_url(url)

        start = time.time()

        response = requests.get(
            url,
            timeout=5
        )

        end = time.time()

        headers = response.headers

        # Target Information

        parsed = urlparse(url)

        domain = parsed.netloc

        # Remove port if the URL contains one
        domain = domain.split(":")[0]

        report["target"] = domain

        report["url"] = url

        # General Information

        report["status"] = response.status_code

        report["response_time"] = round(
            end - start,
            2
        )

        report["server"] = headers.get(
            "Server",
            "Unknown"
        )

        report["content_type"] = headers.get(
            "Content-Type",
            "Unknown"
        )

        # HTTPS CHECK

        report["https"] = (
            parsed.scheme == "https"
        )

        report["ssl"] = check_ssl(domain)

        # DNS CHECK

        try:

            ip = socket.gethostbyname(domain)

            report["ip"] = ip

            report["dns"] = "Resolved Successfully ✅"

        except Exception:

            report["ip"] = "Unknown"

            report["dns"] = "Failed ❌"

        # Security Headers

        security_headers = {

            "Content-Security-Policy":
            "CSP",

            "Strict-Transport-Security":
            "HSTS",

            "X-Frame-Options":
            "Clickjacking Protection",

            "X-Content-Type-Options":
            "MIME Protection",

            "Referrer-Policy":
            "Privacy Protection"

        }

        missing = []

        enabled = []

        for header, name in security_headers.items():

            if header in headers:

                enabled.append(name)

            else:

                missing.append(name)

        report["enabled_headers"] = enabled

        report["missing_headers"] = missing

        # Security Recommendations

        recommendations = []

        if not report["https"]:

            recommendations.append(
                "Enable HTTPS to protect data transmitted between users and the website."
            )

        if "HSTS" in missing:

            recommendations.append(
                "Enable HSTS (Strict-Transport-Security) to enforce secure HTTPS connections."
            )

        if "CSP" in missing:

            recommendations.append(
                "Add a Content-Security-Policy header to help reduce XSS and content injection risks."
            )

        if "Clickjacking Protection" in missing:

            recommendations.append(
                "Add X-Frame-Options to help protect the website against clickjacking."
            )

        if "MIME Protection" in missing:

            recommendations.append(
                "Add X-Content-Type-Options to reduce MIME-sniffing risks."
            )

        if "Privacy Protection" in missing:

            recommendations.append(
                "Configure Referrer-Policy to control how referrer information is shared."
            )

        if not recommendations:

            recommendations.append(
                "No major issues were detected by the current security checks."
            )

        report["recommendations"] = recommendations

        # Risk Assessment

        suspicious = 0

        if not report["https"]:

            suspicious += 20

        suspicious += len(missing) * 10

        if suspicious > 100:

            suspicious = 100

        report["attack_probability"] = suspicious

        # Security Score

        security_score = 0

        if report["https"]:

            security_score += 20

        if report["dns"] == "Resolved Successfully ✅":

            security_score += 15

        security_score += len(enabled) * 13

        if security_score > 100:

            security_score = 100

        report["security_score"] = security_score

        report["risk_score"] = 100 - security_score

        # Risk Level

        if security_score >= 90:

            report["risk"] = "Excellent 🟢"

        elif security_score >= 75:

            report["risk"] = "Good 🟢"

        elif security_score >= 50:

            report["risk"] = "Fair 🟡"

        else:

            report["risk"] = "Poor 🔴"

        # Protection Score

        protection = 100 - suspicious

        report["protection"] = protection

    except Exception as e:

        report["error"] = str(e)

    return report