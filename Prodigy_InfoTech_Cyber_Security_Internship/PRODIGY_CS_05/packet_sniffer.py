from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

def packet_callback(packet):
    # Extract IP information
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        # Determine the protocol
        if TCP in packet:
            protocol = "TCP"
            payload = packet[TCP].payload
        elif UDP in packet:
            protocol = "UDP"
            payload = packet[UDP].payload
        else:
            protocol = "Other"
            payload = packet[IP].payload
        
        # Print packet details
        print(f"Time: {datetime.now()}")
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {protocol}")
        print(f"Payload: {payload}")
        print("="*50)

def main():
    print("Starting packet sniffer...")
    # Capture packets indefinitely
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
