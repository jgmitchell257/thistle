import subprocess
import ipaddress


def check_collab_edge(domain: str):
    edge = "_collab-edge._tls." + domain
    nslookup = subprocess.run(["nslookup", "-type=SRV", edge], encoding="UTF-8", capture_output=True)
    if "NXDOMAIN" in nslookup.stdout:
        return False
    else:
        return True


def ip_from_ping(hostname):
    grab_output = subprocess.run(["ping","-c","4",hostname],capture_output=True)
    bits = grab_output.stdout.decode("utf-8")
    bucket = bits.split()
    ip = bucket[2].strip("[,]")
    if ip == "could":
        ip = "Not found"
    return ip


def ip_from_nslookup(hostname):
    nslookup_raw = subprocess.run(["nslookup",hostname],capture_output=True)
    nslookup_bits = nslookup_raw.stdout.decode("utf-8")
    nslookup_bucket = nslookup_bits.split()   
    try:
        ip = nslookup_bucket[7]
        ipaddress.IPv4Address(ip)
        return ip
    except:
        ip_not_found = "Not found"
        return ip_not_found