#!/usr/bin/python

import json
import socket
import ssl


def get_certificate(host):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
    conn.connect((host, 443))
    cert = conn.getpeercert()
    return cert

hostname =  input("Enter hostname (www.example.com) to check > ")
cert = get_certificate(hostname)
cert_json = json.dumps(cert, indent=4)
print(cert_json)