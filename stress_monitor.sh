#!/bin/bash

# Define the filename for the log file
LOG_FILE="stress_monitor.log"

# Function to get CPU temperature
get_cpu_temp() {
    # Read the CPU temperature from /sys/class/thermal/thermal_zone0/temp
    cpu_temp=$(cat /sys/class/thermal/thermal_zone0/temp)
    # Convert temperature from millidegrees Celsius to degrees Celsius
    cpu_temp=$(echo "scale=2; $cpu_temp / 1000" | bc)
    echo "CPU Temperature: $cpu_temp°C"
}

# Function to get CPU usage
get_cpu_usage() {
    # Use the top command to get CPU usage percentage
    cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    echo "CPU Usage: $cpu_usage%"
}

# Function to get memory usage
get_memory_usage() {
    # Use the free command to get memory usage
    memory_usage=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
    echo "Memory Usage: $memory_usage%"
}

# Function to log data to file
log_data() {
    echo "$(date) - $(get_cpu_temp) | $(get_cpu_usage) | $(get_memory_usage)" >> "$LOG_FILE"
}

# Main function
main() {
    # Check if the log file exists, if not, create it
    if [ ! -f "$LOG_FILE" ]; then
        touch "$LOG_FILE"
    fi

    # Log data every 5 seconds
    while true; do
        log_data
        sleep 5
    done
}

# Execute main function
main
