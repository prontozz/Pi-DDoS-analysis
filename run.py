import socket
import struct
from collections import defaultdict
import csv
from tabulate import tabulate

def analyze_packet(packet):
    # Extracting IP header information
    ip_header = packet[:20]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
    version_ihl = iph[0]
    ihl = version_ihl & 0xF
    iph_length = ihl * 4
    src_ip = socket.inet_ntoa(iph[8])

    # Extracting TCP header information
    tcp_header = packet[iph_length:iph_length+20]
    tcph = struct.unpack('!HHLLBBHHH', tcp_header)
    src_port = tcph[0]

    return src_ip, src_port

def detect_ddos():
    # Initialize a dictionary to store counts of requests by IP address
    request_counts = defaultdict(int)

    # Create a raw socket to capture network packets
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

    print("Detecting DDoS attacks...")
    try:
        while True:
            # Receive a packet
            packet = s.recvfrom(65565)[0]

            # Analyze the packet
            src_ip, src_port = analyze_packet(packet)

            # Increment request count for the source IP
            request_counts[(src_ip, src_port)] += 1

            # Display real-time information in a table
            headers = ["Source IP", "Source Port", "Request Count"]
            table_data = [(ip, port, count) for (ip, port), count in request_counts.items()]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))

            # Save results to a CSV file
            with open("results.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Source IP", "Source Port", "Request Count"])
                writer.writerows(table_data)
                
    except KeyboardInterrupt:
        print("Stopping DDoS detection")

if __name__ == "__main__":
    detect_ddos()
