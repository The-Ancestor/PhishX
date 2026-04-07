import re
import link
import language

def analyze_email_text(field):
    # -- LINK EXTRACTION --
    full_url_pattern = r'https?://[^\s]+'
    domain_pattern = r'\b(?:www\.)?([a-zA-Z0-9-]+\.[a-zA-Z]{2,})\b'

    full_urls = re.findall(full_url_pattern, field)

    if full_urls:
        links = full_urls
    else:
        raw_domains = re.findall(domain_pattern, field)
        links = ["http://" + d for d in raw_domains]

    # -- ANALYSIS --
    language_score = language.language_risk_score(field)
    link_results = link.analyze_links(links)
    total_link_score = sum(item["risk_score"] for item in link_results)
    total_score = language_score + total_link_score

    # -- Risk Level --
    if total_score >= 70:
        risk_level = "HIGH RISK — Likely phishing email"
    elif total_score >= 40:
        risk_level = "MEDIUM RISK — Suspicious content detected"
    else:
        risk_level = "LOW RISK — No strong phishing indicators"

    return {
        "language_score": language_score,
        "total_link_score": total_link_score,
        "total_score": total_score,
        "risk_level": risk_level,
        "links": link_results
    }
