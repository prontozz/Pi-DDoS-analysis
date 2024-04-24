import os
import pandas as pd
import matplotlib.pyplot as plt

# Directory containing the log files
log_dir = 'stressMonitorLogs/'

# List to store DataFrames for each log file
dfs = []

# Loop through each file in the directory
for file in os.listdir(log_dir):
    if file.endswith('.log'):
        # Read the log file into a DataFrame
        df = pd.read_csv(os.path.join(log_dir, file), delimiter=' - ', header=None, engine='python')
        # Extract test description from file name
        test_description = file.split('.')[0]  # Assumes file name format is 'test_description.log'
        # Add comment to DataFrame
        df['Comment'] = f'# Test Description: {test_description}'
        # Rename columns
        df.columns = ['Timestamp', 'CPU Temperature', 'CPU Usage', 'Memory Usage', 'Network Traffic', 'Comment']
        # Convert timestamp to datetime
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        # Append DataFrame to list
        dfs.append(df)

# Plot CPU temperature for each test
plt.figure(figsize=(10, 6))
for i, df in enumerate(dfs, start=1):
    plt.plot(df['Timestamp'], df['CPU Temperature'], label=f'Test {i}')

plt.title('CPU Temperature During DDoS Attacks')
plt.xlabel('Timestamp')
plt.ylabel('CPU Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Save plot as image file (optional)
plt.savefig('cpu_temperature_multiplot.png')

# Show plot
plt.show()
