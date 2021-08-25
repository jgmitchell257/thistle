import subprocess


def check_collab_edge(domain: str):
    edge = "_collab-edge._tls." + domain
    nslookup = subprocess.run(["nslookup", "-type=SRV", edge], encoding="UTF-8", capture_output=True)
    if "NXDOMAIN" in nslookup.stdout:
        return False
    else:
        return True