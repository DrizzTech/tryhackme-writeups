#!/usr/bin/env python3

import subprocess
import platform
import ipaddress
import socket
import sys
import re

def get_private_ip_and_subnet():
    system = platform.system().lower()

    if system == 'windows':
        try:
            output = subprocess.check_output("ipconfig", text=True)
        except Exception as e:
            print(f"Error running ipconfig: {e}")
            sys.exit(1)

        ip_pattern = re.compile(r"IPv4 Address[.\s]*:\s*([\d\.]+)")
        mask_pattern = re.compile(r"Subnet Mask[.\s]*:\s*([\d\.]+)")

        ip_match = ip_pattern.search(output)
        mask_match = mask_pattern.search(output)

        if ip_match and mask_match:
            ip = ip_match.group(1)
            if ip.startswith("127."):
                print("Detected loopback IP on Windows, please check network connection.")
                sys.exit(1)
            return ip, mask_match.group(1)
        else:
            print("Could not find IP or subnet mask in ipconfig output.")
            sys.exit(1)

    else:
        try:
            output = subprocess.check_output(["ip", "addr"], text=True)
        except Exception as e:
            print(f"Error running ip addr: {e}")
            sys.exit(1)

        matches = re.findall(r"inet (\d+\.\d+\.\d+\.\d+)/(\d+)", output)
        for ip, cidr in matches:
            if not ip.startswith("127."):
                mask = str(ipaddress.IPv4Network(f"0.0.0.0/{cidr}").netmask)
                return ip, mask

        print("No non-loopback IP address found.")
        sys.exit(1)

def cidr_from_netmask(netmask):
    return ipaddress.IPv4Network(f"0.0.0.0/{netmask}").prefixlen

def ping(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', '-w', '1000', str(ip)]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def get_hostname(ip):
    try:
        hostname, _, _ = socket.gethostbyaddr(str(ip))
    except socket.herror:
        hostname = "Unknown"
    return hostname

def scan_subnet(subnet):
    active_devices = []
    print(f"Scanning subnet: {subnet}")
    for ip in ipaddress.IPv4Network(subnet):
        if ping(ip):
            hostname = get_hostname(ip)
            print(f"{ip} is active — Hostname: {hostname}")
            active_devices.append((str(ip), hostname))
    return active_devices

if __name__ == "__main__":
    ip, netmask = get_private_ip_and_subnet()
    cidr = cidr_from_netmask(netmask)
    network = ipaddress.IPv4Network(f"{ip}/{cidr}", strict=False)
    subnet = str(network)
    scan_subnet(subnet)
