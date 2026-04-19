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
