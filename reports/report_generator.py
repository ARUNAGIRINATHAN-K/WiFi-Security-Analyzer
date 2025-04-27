import os

def generate_report(results):
    report_path = "reports/security_report.txt"
    os.makedirs(os.path.dirname(report_path), exist_ok=True)

    with open(report_path, "w") as f:
        f.write("WiFi Security Analysis Report\n")
        f.write("===============================\n\n")

        for res in results:
            f.write(f"SSID: {res['ssid']}\n")
            f.write(f"BSSID: {res['bssid']}\n")
            f.write(f"Signal Strength: {res['signal']}\n")
            f.write("Security Issues:\n")
            if res['issues']:
                for issue in res['issues']:
                    f.write(f"- {issue}\n")
            else:
                f.write("- No major issues detected.\n")
            f.write("\n")

    print(f"📄 Report generated at {report_path}")
