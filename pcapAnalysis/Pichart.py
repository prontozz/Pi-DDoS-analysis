import pandas as pd
import os
import matplotlib.pyplot as plt

def process_csv_files(input_folder):
    ip_activity = {}

    for file in os.listdir(input_folder):
        if file.endswith('.csv'):
            csv_file = os.path.join(input_folder, file)
            df = pd.read_csv(csv_file)

            # Count the number of packets sent by each source IP address
            for ip in df['Source IP']:
                if ip in ip_activity:
                    ip_activity[ip] += 1
                else:
                    ip_activity[ip] = 1

    return ip_activity

def create_pie_chart(ip_activity):
    # Sort IP addresses by activity (number of packets sent)
    sorted_ip_activity = sorted(ip_activity.items(), key=lambda x: x[1], reverse=True)
    top_ips = dict(sorted_ip_activity[:10])  # Select top 10 IPs for visualization

    # Create pie chart
    labels = top_ips.keys()
    sizes = top_ips.values()

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Top 10 Source IP Addresses by Packet Activity')
    plt.show()

if __name__ == "__main__":
    input_folder = r"C:\Users\Oliver\Pi-DDoS-analysis\CsvFiles"
    ip_activity = process_csv_files(input_folder)
    create_pie_chart(ip_activity)
