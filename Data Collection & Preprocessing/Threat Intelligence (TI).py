import requests
                                                                                    
def fetch_threat_intel_report(indicator, api_key, api_endpoint):
    headers = {"x-api-key": api_key} # Or other authentication methods
    params = {"query": indicator} # Or other query parameters

    try: 
        response = requests.get(api_endpoint, headers=headers, params=params)
        response.raise_for_status() # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching TI for {indicator}: {e}")
        return None

# Usage:
# vt_api_key = "YOUR_VIRUSTOTAL_API_KEY"
# ip_to_check = "8.8.8.8"
# vt_report = fetch_threat_intel_report(ip_to_check, vt_api_key, "https://www.virustotal.com/api/v3/ip_addresses/")
# if vt_report:
#     print("VirusTotal report for", ip_to_check, ":", vt_report)
