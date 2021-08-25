#!/usr/bin/python

import re
import lxml.html.clean
from selenium import webdriver


def cleanme(content: str) -> str:
    cleaner = lxml.html.clean.Cleaner(
        allow_tags=["div"],
        kill_tags=["header", "nav", "noscript", "h3", "h4"],
        remove_unknown_tags=False,
        scripts=True,
        style=True,
    )
    html = lxml.html.document_fromstring(content)
    html_clean = cleaner.clean_html(html)
    return html_clean.text_content().strip()


def get_webex_status():
    firefox_options = webdriver.firefox.options.Options()
    firefox_options.headless = True
    browser = webdriver.Firefox(options=firefox_options)
    browser.get("https://status.webex.com")
    page_html = browser.page_source
    cleaned = cleanme(page_html)
    return cleaned


def get_header_position(search_string):
    string_match = re.search(search_string, cleaned)
    if string_match:
        return string_match.span()[0]
    else:
        print(f"Couldn't find __{search_string}__ in the text. Exiting script.")
        exit()


def print_states(section: str) -> list:
    """Builds human friendly output from a list of services and states"""
    services = []
    states = []
    wbx_service = section.split("  ")
    print(wbx_service.pop(0) + "\n" + "-" * 79)

    for (k, i) in enumerate(wbx_service):
        if k % 2:
            states.append(i.strip())
        else:
            services.append(i.strip())

    wbx = list(zip(services, states))

    for i in wbx:
        print(f"{i[0]} - {i[1]}")
    print("\n")


if __name__ == "__main__":
    cleaned = get_webex_status()
    # print(cleaned)

    # Get positions of the section headers
    webex_meetings = get_header_position("Webex Meetings")
    webex_app = get_header_position("Webex App")
    webex_control_hub = get_header_position("Webex Control Hub")
    webex_cloud_registered_device = get_header_position("Webex Cloud Registered Device")
    webex_calling = get_header_position("Webex Calling \(Spark Call\)")
    webex_hybrid_services = get_header_position("Webex Hybrid Services")
    developer_api = get_header_position("Developer API")
    webex_contact_center = get_header_position("Webex Contact Center")
    ucm_cloud = get_header_position("UCM Cloud")
    webex_for_broadworks = get_header_position("Webex for BroadWorks")

    # Get section details
    wbx_mtg = cleaned[webex_meetings:webex_app]
    wbx_app = cleaned[webex_app:webex_control_hub]
    wbx_ch = cleaned[webex_control_hub:webex_cloud_registered_device]
    wbx_crd = cleaned[webex_cloud_registered_device:webex_calling]
    wbx_c = cleaned[webex_calling:webex_hybrid_services]
    wbx_hs = cleaned[webex_hybrid_services:developer_api]
    wbx_da = cleaned[developer_api:webex_contact_center]
    wbx_cc = cleaned[webex_contact_center:ucm_cloud]
    ucmc = cleaned[ucm_cloud:webex_for_broadworks]
    wbx_b = cleaned[webex_for_broadworks::]

    # Print section details
    print_states(wbx_mtg)
    print_states(wbx_app)
    print_states(wbx_ch)
    print_states(wbx_crd)
    print_states(wbx_c)
    print_states(wbx_hs)
    print_states(wbx_da)
    print_states(wbx_cc)
    print_states(ucmc)
    print_states(wbx_b)

    
