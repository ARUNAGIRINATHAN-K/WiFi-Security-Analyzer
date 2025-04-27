import pywifi
from pywifi import const
import time

def scan_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()  # Start scanning

    # --- New part: Keep checking until scan is ready ---
    scan_results = []
    timeout = 10  # seconds
    start_time = time.time()

    while True:
        time.sleep(1)  # wait 1 sec before checking
        scan_results = iface.scan_results()

        if scan_results:
            break  # success, got some networks

        if time.time() - start_time > timeout:
            print("[!] Scan timeout. No networks found.")
            return []

    # --- Proceed normally ---
    networks = []
    for network in scan_results:
        network_info = {
            "ssid": network.ssid,
            "bssid": network.bssid,
            "signal": network.signal,
            "encryption": get_encryption_type(network)
        }
        networks.append(network_info)

    return networks

def get_encryption_type(network):
    if network.akm:
        return network.akm[0]
    elif network.auth:
        return network.auth[0]
    else:
        return "Unknown"
