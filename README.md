## Pi-DDoS Analysis

### Mitigation strategies for IoT devices against DDoS attacks


This repository contains data collection and analysis scripts for my dissertation project using python and bash for this, required packages can be found within the requirements.txt document.

### Overview of Files

Below is a list/table providing an overview of each file in this repository:

- **stress_monitor.sh:** Used to log the system for various time intervals when run taking the CPU temprature, usage and memory usage.
- **stressplotting.py:** Used to analyse the stress monitor log files and plot the data onto a graph.
- **pcaptoCsv.py:** Converts the wireshark Pcap files into a CSV format for analysis.
- **Pichart.py:** Reads all of the Pcap files within the specified directory and sorts which device sent the most packets from the DDoS attack into a Pichart format.
- **stressHeatIncrease.py:** Reads a stress monitor file for the CPU temp increase to determine system stress
- **temp:**

Requirements

To run the scripts in this repository, you'll need the following:

Python

    [python pythonscriptname.py ]
    

Bash script

    sudo chmod +777 ./script.sh
    ./script.sh
    

## Results
### Overview

Results gathered from the testing conducted for the dissertation will be displayed here to display the use of the scripts and how the data should be processed and displayed to the user.

## Filler for now:
Images

[Include any images or visualizations generated from your data analysis. Provide a brief description or explanation for each image.]
Image 1: [Title/Description]


Explanation: [Briefly explain what the image shows and its significance]
Image 2: [Title/Description]


Explanation: [Briefly explain what the image shows and its significance]
Data Analysis

[Include any additional analysis or findings from your data, providing explanations or insights gained]