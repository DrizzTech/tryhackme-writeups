# IP Adress Finder

import socket
import requests

# Get internal (local) IP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"Internal IP: {local_ip}")

# Get external (public) IP
try:
    external_ip = requests.get('https://api.ipify.org').text
    print(f"External IP: {external_ip}")
except requests.RequestException:
    print("Could not get external IP")
