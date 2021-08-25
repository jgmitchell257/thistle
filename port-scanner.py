#!/bin/python
import argparse
import socket


parser = argparse.ArgumentParser(
    description="Simple port scanner", 
    usage="./port-scanner.py --host=host.example.com"
)
parser.add_argument("--host", required=True, help="Host to port scan")
args = parser.parse_args()

# Common ports used by Cisco servers
ports = {
    21: "FTP",
    22: "SSH", 
    23: "telnet",
    69: "TFTP",
    80: "HTTP", 
    443: "Secure HTTP", 
    5060: "SIP", 
    5061: "Secure SIP", 
    6970: "Cisco phone/Jabber TFTP",
    8443: "Cisco secure HTTP/UDS",
}

def is_port_open(host, port):
    s = socket.socket()
    s.settimeout(0.9)
    try:
        s.connect((host, port))
    except:
        return False
    else:
        return True

for port in ports:
    if is_port_open(args.host, port):
        print(f"[+] {args.host}:{port} - {ports[port]}")
    else:
        print(f"[-] {args.host}:{port} - {ports[port]}")