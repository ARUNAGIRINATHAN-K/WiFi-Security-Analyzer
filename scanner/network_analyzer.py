def analyze_network(network_info):
 
    analysis = {}

    encryption = network_info.get('encryption', 'Unknown')
    if encryption == "WEP":
        analysis['encryption_issue'] = "⚠️ Very Weak (WEP is outdated and insecure)"
    elif encryption == "Open":
        analysis['encryption_issue'] = "⚠️ No Password Protection (Open Network)"
    elif encryption == "WPA-PSK":
        analysis['encryption_issue'] = "⚠️ Weak (Use WPA2 or WPA3 instead)"
    elif encryption == "WPA2-PSK":
        analysis['encryption_issue'] = "✅ Good (WPA2 is secure if a strong password is used)"
    elif encryption == "WPA3-PSK":
        analysis['encryption_issue'] = "✅ Excellent (WPA3 is currently the best)"
    else:
        analysis['encryption_issue'] = "❓ Unknown Encryption"

    if "WPS" in network_info.get('ssid', '').upper():
        analysis['wps_issue'] = "⚠️ WPS detected in SSID name (may indicate WPS is ON)"
    else:
        analysis['wps_issue'] = "ℹ️ WPS status unknown (Manual check recommended)"

    return analysis
