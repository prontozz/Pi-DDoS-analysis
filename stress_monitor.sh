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

# Function to get network interface traffic
get_network_traffic() {
    # Use the ifconfig command to get network interface traffic statistics
    network_traffic=$(ifconfig eth0 | grep "RX bytes\|TX bytes")
    echo "$network_traffic"
}

# Function to log data to file
log_data() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $(get_cpu_temp) | $(get_cpu_usage) | $(get_memory_usage) | $(get_network_traffic)" >> "$LOG_FILE"
}

# Function for countdown
countdown() {
    secs=$1
    while [ $secs -gt 0 ]; do
        echo -ne "Starting in $secs seconds...\033[0K\r"
        sleep 1
        : $((secs--))
    done
    echo "Starting now!"
}

# Main function
main() {
    # Check if the log file exists, if not, create it
    if [ ! -f "$LOG_FILE" ]; then
        touch "$LOG_FILE"
    fi

    # Display options for logging interval
    echo "Select the time interval for logging data:"
    echo "1. Every 500ms"
    echo "2. Every 1s"
    echo "3. Every 3s"
    read -p "Enter your choice (1/2/3): " choice

    case $choice in
        1) interval=0.5 ;; 
        2) interval=1 ;;
        3) interval=3 ;;
        *) echo "Invalid choice. Defaulting to logging every 1 second."; interval=1 ;;
    esac

    # Countdown before starting
    countdown 5

    # Log data at specified interval
    while true; do
        log_data
        # Ensure the log occurs precisely at the beginning of the next second
        sleep $(echo "scale=3; $interval - $(date +%N) / 1000000000" | bc)
    done
}

# Execute main function
main
