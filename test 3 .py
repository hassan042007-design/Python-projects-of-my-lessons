import scapy.all as scapy

def scan(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    devices = []
    for element in answered:
        devices.append({"ip": element[1].psrc, "mac": element[1].hwsrc})
    return devices

if __name__ == "__main__":
    # Replace with your Wi-Fi subnet, e.g. 192.168.1.1/24
    network = "192.168.1.1/24"
    results = scan(network)

    print("Devices connected to your Wi-Fi:")
    for device in results:
        print(f"IP: {device['ip']}  |  MAC: {device['mac']}")
