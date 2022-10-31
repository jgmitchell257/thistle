import concurrent.futures
import logging
import re
import threading
import time
import paramiko
from paramiko_expect import SSHClientInteraction
import traceback

USERNAME = "username"
PASSWORD = "password"

def collect(server: str) -> str:
    save_file = "output/" + server + ".txt"
    HOSTNAME = server
    PROMPT = "admin:"
    print(f"Connecting to {server}")
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOSTNAME, username=USERNAME, password=PASSWORD, allow_agent=False, look_for_keys=False)

        with SSHClientInteraction(client, timeout=120, display=False) as interact:
            interact.expect(PROMPT)
            banner = interact.current_output_clean
            logging.info(banner)
            time.sleep(2)
            interact.send("run sql select eu.firstname,eu.lastname,eu.userid,d.ndescription from enduser as eu, device as d, extensionmobilitydynamic as emd where emd.fkenduser = eu.pkid and emd.fkdevice = d.pkid")
            interact.expect(PROMPT)
            ext_mobility = interact.current_output_clean
            logging.info(ext_mobility)

            with open(save_file, "w") as f:
                f.writelines(ext_mobility)

            interact.send("logout")

    except Exception:
        traceback.print_exc()

        return "Failure"
    finally:
        try:
            client.close()
        except Exception:
            pass
    

if __name__ == "__main__":
    # logging.basicConfig(filename="ssh.log", level=logging.INFO)
    source_file = open("input.txt", "r")
    dirty_list = source_file.readlines()
    servers = []
    for a in dirty_list:
        server_name = a.strip("\n")
        servers.append(server_name)

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(collect,servers)