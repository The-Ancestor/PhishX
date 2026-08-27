PhishX

PhishX is a web-based email phishing analyzer built with **Flask**. It analyzes email content and links to provide a **risk score**, helping you detect potential phishing attacks.

Live and running on AWS EC2
💻 Live demo: http://34.228.41.8:8080


-- Features --

  - **Language Analysis:** Scores the email content for suspicious language patterns.
  - **Link Analysis:** Extracts URLs and checks for:
  - HTTP/HTTPS protocol risks
  - Suspicious top-level domains (TLDs)
  - Double extensions (e.g., `.exe`, `.zip`)
  - Subdomain anomalies
  - Brand impersonation
  - URL obfuscation (e.g., IP addresses, `@` symbols)
  - **Risk Assessment:** Combines language and link scores to give an overall **risk level**:
  - `LOW RISK` — Safe
  - `MEDIUM RISK` — Suspicious
  - `HIGH RISK` — Likely phishing

  - Architecture & Tech Stack

    Backend Framework: Python 3.10+, Flask

    Parsing & Heuristics: urllib.parse, Regular Expressions (Regex)

    Infrastructure: AWS EC2 (Ubuntu Linux)

    WSGI / Web Server: Gunicorn

    🚀 Quickstart (Local Development)
Prerequisites

    Python 3.10 or higher

    pip package manager

Installation

    Clone the repository:

git clone https://github.com/The-Ancestor/PhishX.git <br>
cd PhishX <br>

Create and activate a virtual environment:

python3 -m venv venv <br>
source venv/bin/activate  # On Windows: venv\Scripts\activate <br>

Install dependencies:

pip install -r requirements.txt <br>

Run the application:
python app.py

Navigate to [http://127.0.0.1:8080](http://127.0.0.1:8080) in your web browser.
