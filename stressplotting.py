import matplotlib.pyplot as plt
import datetime
import os

# Function to read data from log file
def read_data_from_log(log_file):
    timestamps = []
    cpu_temperatures = []

    with open(log_file, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split(" - ")
            timestamp = parts[0]
            temperature_part = parts[1].split(" | ")[0]

            try:
                cpu_temp = float(temperature_part.split(":")[1].strip().rstrip("°C"))
                timestamps.append(timestamp)
                cpu_temperatures.append(cpu_temp)
            except ValueError:
                # Ignore lines that cannot be parsed correctly
                pass
    
    return timestamps, cpu_temperatures

# Find the log file with .log extension in the current directory
log_files = [f for f in os.listdir() if f.endswith('.log')]
if len(log_files) == 0:
    print("No .log file found in the current directory.")
    exit()

# Assume the first found log file is the one to analyze
log_file = log_files[0]
print(f"Analyzing data from {log_file}...")

# Read data from log file
timestamps, cpu_temperatures = read_data_from_log(log_file)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(timestamps, cpu_temperatures, marker='o', linestyle='-')
plt.title('CPU Temperature Over Time')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
