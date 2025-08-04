# Example using scapy to read a PCAP and extract basic info
from scapy.all import rdpcap, IP, TCP, UDP
 
packets = rdpcap("your_network_traffic.pcap")
features = []

for pkt in packets:   
    if IP in pkt:
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        protocol = pkt[IP].proto
        # Extract more features: port numbers, packet length, etc.
        if TCP in pkt:
            src_port = pkt[TCP].sport
            dst_port = pkt[TCP].dport
        elif UDP in pkt:
            src_port = pkt[UDP].sport
            dst_port = pkt[UDP].dport
        else:
            src_port, dst_port = 0, 0 # Or handle based on protocol

        features.append([src_ip, dst_ip, protocol, src_port, dst_port, len(pkt)])
# You'll need to convert IPs to numerical representations for ML
# E.g., using ipaddress module or simple integer mapping
