import os
import sys
from scapy.all import *
from collections import defaultdict
from tabulate import tabulate
from tqdm import tqdm

def analyze_pcap(pcap_file):
    packets = rdpcap(pcap_file)

    ip_counter = defaultdict(int)

    # Count packets and update progress bar
    progress_bar = tqdm(total=len(packets), desc="Analyzing Packets", unit="pkt")
    for packet in packets:
        progress_bar.update(1)
        if IP in packet:
            src_ip = packet[IP].src
            ip_counter[src_ip] += 1
    progress_bar.close()

    # Create a table with important data for DDoS attacks
    table_data = []
    for src_ip, count in ip_counter.items():
        table_data.append([src_ip, count])

    headers = ["Source IP", "Packet Count"]

    # Print table
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    # Save table to a text file
    output_file = pcap_file + "_analysis.txt"
    with open(output_file, "w") as file:
        file.write(tabulate(table_data, headers=headers, tablefmt="grid"))
    print(f"Analysis results saved to: {output_file}")

def select_pcap():
    pcap_files = [file for file in os.listdir() if file.endswith(".pcap") or file.endswith(".pcapng")]

    if not pcap_files:
        print("No pcap or pcapng files found in the directory.")
        sys.exit(1)

    print("PCAP/PCAPNG files found in the directory:")
    for idx, file in enumerate(pcap_files, start=1):
        print(f"{idx}. {file}")

    selection = input("Enter the number of the PCAP/PCAPNG file to analyze: ")
    try:
        selection = int(selection)
        if selection < 1 or selection > len(pcap_files):
            raise ValueError
    except ValueError:
        print("Invalid selection.")
        sys.exit(1)

    return pcap_files[selection - 1]

if __name__ == "__main__":
    pcap_file = select_pcap()
    analyze_pcap(pcap_file)
