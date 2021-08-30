"""
UDS lookup for CUCM
~~~~~~~~~~~~~~~~~~~

Used to process the exported_users.csv file from Webex Control Hub and extract the usernames, then checks the UCM to see if they exist.

Usage:
    >>> process_csv("exported_users.csv")
    >>> users = load_users("userlist.txt")
    >>> check_uds(users, "cucm-publisher.example.com")
"""

import csv
import requests
import urllib3
import xmltodict


def process_csv(filename):
    """Used to extract the usernames from exported_users.csv from the Webex Control Hub"""
    with open(filename, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                with open("userlist.txt", "a") as f:
                    f.write(row["User ID/Email (Required)"] + "\n")


def load_users(user_file) -> list:
    """Creates a userlist from the exported users"""
    with open(user_file, "r") as ul:
        users = ul.readlines()
    users = [user.strip("\n") for user in users]
    return users


def check_uds(users: list, server: str, un_format=None):
    """Performs UDS lookup against CUCM to verfiy if username or email are present

    Arguments:
        users (list): list of users to itterate through
        server (str): resolvable hostname, FQDN or IP address of server to check against
        un_format: username or email
    """
    urllib3.disable_warnings()
    with open("uds_results.txt", "w") as f:
        for u in users:
            if un_format == "email":
                x = requests.get(
                    f"https://{server}:8443/cucm-uds/clusterUser?email={u}",
                    verify=False,
                )
            else:
                x = requests.get(
                    f"https://{server}:8443/cucm-uds/clusterUser?username={u}",
                    verify=False,
                )
            d = xmltodict.parse(x.text)
            f.write(u + " - " + d["clusterUser"]["result"]["@found"] + "\n")
    return "Wrote uds_results.txt"
