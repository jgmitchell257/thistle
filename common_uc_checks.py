#!/usr/bin/python

"""
common_uc_checks
----------------
Simple script to check for common configurations on Cisco UC servers.

Usage:
    $ python common_uc_checks.py
    Enter server to check > ucm-publisher.example.com

    Checking ucm-publisher.example.com
    --------------------------------------------------------------------------------
    [+] jabber-config.xml

"""

import requests


server = input("Enter server to check > ")
print(f"\nChecking {server}\n" + "-" * 80)

jabber_config = requests.get(f"http://{server}:6970/jabber-config.xml")
if jabber_config:
    print("[+] jabber-config.xml")
else:
    print("[-] jabber-config.xml")

print("\n")