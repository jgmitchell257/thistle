"""
patterns
--------
Common regex patterns for including in scripts.
"""


us_phone = r"\(\d\d\d\) \d\d\d-?\d\d\d\d"
short_date = r"\d?\d/\d?\d/\d\d\d\d"
ssn = r"\d\d\d-\d\d-\d\d\d\d"
time_format = r"[0-9]?[0-9]:[0-9][0-9]"
zip_code = r"\d{5}-\d{4}|\d{5}"
last_first = r"([\w\-]+)\s*,\s*(\w+)\s*"
ip_address = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
mac_address = r"(?:[0-9a-fA-F]{2}\:){5}[0-9a-fA-F]{2}"
port_number = r"\d{1,5}"
protocol = r"(TCP|UDP|ICMP|GRE)"
email_address = r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
url = r"(http(s)?://)?([\w-]+\.)+[\w-]+[.com]+(/[/?%&=]*)?"
