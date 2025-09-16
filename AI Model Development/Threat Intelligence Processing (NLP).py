import re          
   
def extract_iocs_from_text(report_text):
    # These are simple regex patterns. Real-world would be more complex.
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    domain_pattern = r"\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}\b"
    hash_pattern = r"\b[0-9a-fA-F]{32}|[0-9a-fA-F]{40}|[0-9a-fA-F]{64}\b" # MD5, SHA1, SHA256

    ips = re.findall(ip_pattern, report_text)
    domains = re.findall(domain_pattern,  report_text)
    hashes = re.findall(hash_pattern, report_text)

    return {'ips': ips, 'domains': domains, 'hashes': hashes}

# Usage:
# threat_report_content = "Malicious activity from 192.168.1.100, connecting to evil.com. Malware hash: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6."
# extracted_iocs = extract_iocs_from_text(threat_report_content)
# print("Extracted IOCs:", extracted_iocs)
