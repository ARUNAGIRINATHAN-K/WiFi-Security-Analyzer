from scanner.wifi_scanner import scan_networks
from scanner.network_analyzer import analyze_network
from scanner.password_checker import check_password_strength
from reports.report_generator import generate_report
from utils.helpers import banner


def main():
    print("🔍 Starting WiFi Security Analyzer...\n")
    networks = scan_networks()
    
    if not networks:
        print("❌ No networks found. Please check your WiFi adapter.")
        return

    print(f"\n📡 {len(networks)} network(s) found:\n")
    for idx, net in enumerate(networks):
        print(f"{idx + 1}. SSID: {net['ssid']} | Signal: {net['signal']} | Encryption: {net['encryption']}")

    
    try:
        choice = int(input("\nEnter the number of the network you want to analyze: ")) - 1
        selected_network = networks[choice]
    except (ValueError, IndexError):
        print("⚠️ Invalid choice.")
        return

    print(f"\n🔎 Analyzing network: {selected_network['ssid']}...\n")

    
    analysis = analyze_network(selected_network)

    
    password = input("🔑 Enter the WiFi password for this network (or press Enter to skip): ").strip()
    if password:
        strength = check_password_strength(password)
        analysis['password_strength'] = strength

    generate_report(selected_network, analysis)

    print("\n✅ Analysis complete. Report saved successfully!")

if __name__ == "__main__":
    main()
