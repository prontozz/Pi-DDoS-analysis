from scapy.all import *
import pandas as pd
import os

def extract_data_from_pcap(pcap_file):
    packets = rdpcap(pcap_file)
    data = []

    for packet in packets:
        # Check if the 'IP' layer is present
        if IP in packet:
            # Extract relevant data from the packet
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst
            protocol = packet['IP'].proto
            timestamp = packet.time

            data.append([src_ip, dst_ip, protocol, timestamp])

    return data

def save_to_csv(data, output_file):
    df = pd.DataFrame(data, columns=['Source IP', 'Destination IP', 'Protocol', 'Timestamp'])
    df.to_csv(output_file, index=False)

def process_pcap_files(input_folder, output_folder):
    for file in os.listdir(input_folder):
        if file.endswith('.pcapng'):
            pcap_file = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, file.replace('.pcapng', '.csv'))

            data = extract_data_from_pcap(pcap_file)
            save_to_csv(data, output_file)
            print(f"Data from {pcap_file} saved to {output_file}")

if __name__ == "__main__":
    input_folder = "C:/Users/Olive/Pi-DDoS-analysis/pcapfiles"
    output_folder = r"C:\Users\Olive\Pi-DDoS-analysis\CsvFiles"
    process_pcap_files(input_folder, output_folder)
