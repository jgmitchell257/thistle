# thistle

Collection of Python tools and functions. Created and used by me on the regular.

May or may not be useful to others.

## Tools
### get_wbx_status.py
Pulls status for Webex based services from https://status.webex.com/ and displays them in human friendly CLI output.
```
Webex Meetings
-------------------------------------------------------------------------------
Access Webex URL - Operational
Start/join meetings - Operational
Video Platform - Operational
Join audio via VoIP or share video - Operational
Join audio via Telephony - Operational
Schedule meetings - Operational
Share content - Operational
```
### port-scanner.py
Simple port scanner for demonstration purposes.
```
$ python port-scanner.py --host google.com
[-] google.com:21 - FTP
[-] google.com:22 - SSH
[-] google.com:23 - telnet
[-] google.com:69 - TFTP
[+] google.com:80 - HTTP
[+] google.com:443 - Secure HTTP
[-] google.com:5060 - SIP
[-] google.com:5061 - Secure SIP
[-] google.com:6970 - Cisco phone/Jabber TFTP
[-] google.com:8443 - Cisco secure HTTP/UDS
```
