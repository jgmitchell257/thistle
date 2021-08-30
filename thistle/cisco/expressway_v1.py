"""
expressway
~~~~~~~~~~~~~~~~~~~

Easy to use Expressway API functions

Usage:
    >>> demoserver = expressway.Expressway('exp.example.com', 'username', 'password')
    >>> demoserver
    exp.example.com
    >>> demoserver.base_uri
    'https://exp.example.com/api/provisioning'
    >>> 

"""

import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Expressway:
    """
    base class to define an expressway server and set base URLs for the API

    Args:
        hostname: resolvable name of server in string format
        username: admin username for accessing the web GUI
        password: admin password for accessing the web GUI
    """
    def __init__(self, hostname: str, username: str, password: str):
        self.hostname = hostname
        self.exp_user = username
        self.exp_pass = password
        self.base_uri = "https://" + hostname + "/api/provisioning"
        self.cert_uri = self.base_uri + "/certs/server"
        self.credential_uri = self.base_uri + "/common/credential"
        self.dnsserver_uri = self.base_uri + "/common/dns/dnsserver"
        self.dns_zones_uri = self.base_uri + "/common/zone/dnszone"
        self.domain_uri = self.base_uri + "/common/domain"
        self.mra_uri = self.base_uri + "/common/mra"
        self.sip_config_uri = self.base_uri + "/common/protocol/sip/configuration"
        self.searchrule_uri = self.base_uri + "/common/searchrule"
        self.ntpserver_uri = self.base_uri + "/common/time/ntpserver"
        self.ntpstatus_uri = self.base_uri + "/common/time/status"
        self.timezone_uri = self.base_uri + "/common/time/timezone"

    def __repr__(self):
        return self.hostname

    def getCert(self) -> str:
        """Gets the server certificate and returns it as a string

        -----BEGIN CERTIFICATE-----\r\nMIIH8jCCBtqgAwIBAgIJAJG2TBQo8/+EMA0GCSqG...
        
        Args:
            None
        
        Returns:
            server certificate string
        """
        response = requests.get(self.cert_uri, verify=False, auth=(self.exp_user, self.exp_pass))
        return response
    
    def getCredentials(self) -> list:
        """
        Returns list of configured usernames for traversal zones
        """
        response = requests.get(self.credential_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response

    def createCredentials(self, json):
        response = requests.post(self.credential_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def updateCredentials(self, json):
        response = requests.put(self.credential_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def deleteCredentials(self, username):
        response = requests.delete(self.credential_uri, verify=False, auth=(self.exp_user, self.exp_pass), json={"Name": username})
        return response
    
    def getDNSServer(self) -> dict:
        """ Returns dictionary of configured DNS servers """
        response = requests.get(self.dnsserver_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response
    
    def createDNSServer(self, json):
        response = requests.post(self.dnsserver_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def updateDNSServer(self, json):
        response = requests.put(self.dnsserver_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def deleteDNSServer(self, server_index):
        response = requests.delete(self.dnsserver_uri, verify=False, auth=(self.exp_user, self.exp_pass), json={"index": server_index})
        return response

    def getDNSZones(self) -> list:
        response = requests.get(self.dns_zones_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response
    
    def getDomain(self) -> list:
        """ Returns list of configured domains and features """
        response = requests.get(self.domain_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response
    
    def updateDomain(self, json):
        response = requests.post(self.domain_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def updateDomain(self, json):
        response = requests.put(self.domain_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def deleteDomain(self, domain_name):
        response = requests.delete(self.domain_uri, verify=False, auth=(self.exp_user, self.exp_pass), json={"Name": domain_name})
        return response
    
    def getMRA(self) -> dict:
        """ 
        Returns dictionary of configuerd MRA features 
        
        Exmaple:
            {'SSO': 'Off', 'Enabled': 'On'}
        """
        response = requests.get(self.mra_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response
    
    def updateMRA(self, json):
        response = requests.put(self.mra_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def getSIPConfig(self) -> list:
        """
        Returns list of SIP configurations

        Example:
            [{'UdpMode': 'On', 'MutualTlsMode': 'On', 'TlsMode': 'On', 
            'TcpMode': 'On', 'TlsPort': 5061, 'MutualTlsPort': 5062, 
            'TcpOutboundPortStart': 25000, 'UdpPort': 5060, 
            'MinSessionRefreshInterval': 500, 'SipMode': 'On', 'TcpPort': 5060, 
            'SessionRefreshInterval': 1800, 'TlsHandshakeTimeout': 5, 
            'TcpOutboundPortEnd': 29999}]
        """

        response = requests.get(self.sip_config_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response
    
    def updateSIPConfig(self, json):
        response = requests.put(self.sip_config_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def getSearchRule(self) -> list:
        """
        Return list of configured search rules in dictionary format

        Example:
            [{'SIPVariant': 'Any', 'Protocol': 'Any', 'Name': 'LocalZoneMatch', 
            'ReplaceString': '', 'Source': 'Any', 'SourceName': '', 
            'MustAuthenticateRequest': 'No', 'PatternString': '', 
            'Priority': 50, 'OnSuccessfulMatch': 'Continue', 'State': 'Enabled', 
            'Mode': 'AnyAlias', 'Description': 'Default rule: queries the Local Zone for any alias', 
            'SystemGenerated': 'No', 'PatternBehavior': 'Strip', 
            'TargetName': 'LocalZone', 'PatternType': 'Prefix'}]
        """
        response = requests.get(self.searchrule_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response
    
    def createSearchRule(self, json):
        response = requests.post(self.searchrule_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def updateSearchRule(self, json):
        response = requests.put(self.searchrule_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def deleteSearchRule(self, searchrule_name):
        response = requests.put(self.searchrule_uri, verify=False, auth=(self.exp_user, self.exp_pass), json={"Name": searchrule_name})
        return response
    
    def getNTPServer(self) -> list:
        """
        Returns list of configrued NTP servers in dictionary format

        Example:
            [
                {'index': 2, 'KeyId': 1, 'Hash': 'sha1', 'Authentication': 'disabled', 'Address': '173.224.157.252'}, 
                {'index': 1, 'KeyId': 1, 'Hash': 'sha1', 'Authentication': 'disabled', 'Address': '173.224.149.136'}, 
                {'index': 3, 'KeyId': 1, 'Hash': 'sha1', 'Authentication': 'disabled', 'Address': '199.38.38.3'}
            ]
        """
        response = requests.get(self.ntpserver_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response
    
    def createNTPServer(self, json):
        response = requests.post(self.ntpserver_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def updateNTPServer(self, json):
        response = requests.put(self.ntpserver_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def deleteNTPServer(self, ntpserver_index):
        response = requests.put(self.ntpserver_uri, verify=False, auth=(self.exp_user, self.exp_pass), json={"index": ntpserver_index})
        return response
    
    def getNTPStatus(self) -> dict:
        """Returns dictionary of current NTP statuses for each configured NTP server"""
        response = requests.get(self.ntpstatus_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response
    
    def getTimeZone(self) -> dict:
        """Returns dictionary of configrued timezone

        Example:
            {'TimeZone': 'US/Eastern'}
        """

        response = requests.get(self.timezone_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response
    
    def updateTimeZone(self, tz):
        response = requests.put(self.timezone_uri, verify=False, auth=(self.exp_user, self.exp_pass), json={"TimeZone":tz})
        return response
    

class ExpCore(Expressway):
    """Child class to define an expressway-c server and functions specific to Core servers"""
    role = "Core"
    def __init__(self, hostname, username, password):
        super().__init__(hostname, username, password)
        self.cucm_uri = self.base_uri + "/controller/server/cucm"
        self.imp_uri = self.base_uri + "/controller/server/imp"
        self.uc_zone_uri = self.base_uri + "/controller/zone/unifiedcommunicationstraversal"
    
    def getCUCM(self) -> list:
        """Returns list of configured CUCM publishers and their settings

        Example:
            [
                {'Publisher': 'expc.domain.com', 'AesGcm': 'on', 
                'TlsVerify': 'On', 'AxlUsername': 'admin', 
                'SipUpdateForSessionRefresh': 'off', 'IcePassthrough': 'on'}
            ]
        """
        response = requests.get(self.cucm_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response
    
    def createCUCM(self, json):
        response = requests.post(self.cucm_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def deleteCUCM(self, publisher_name):
        response = requests.delete(self.cucm_uri, verify=False, auth=(self.exp_user, self.exp_pass), json={"Publisher":publisher_name})
        return response
    
    def getIMP(self) -> list:
        """Returns list of configured IM&P servers in dictionary format.

        Example:
            [
                {'Publisher': 'imp-publisher.example.com', 'AxlUsername': 'admin', 'TlsVerify': 'On'}
            ]
        """
        response = requests.get(self.imp_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response
    
    def createIMP(self, json):
        response = requests.post(self.imp_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def deleteIMP(self, publisher_name):
        response = requests.delete(self.imp_uri, verify=False, auth=(self.exp_user, self.exp_pass), json={"Publisher":publisher_name})
        return response

    def getUCTraversalZone(self) -> list:
        """Returns list of configured traversal zones and settings in dictionary format

        Example:
            [
                {'Status': 'Active', 'RetryInterval': 120, 'SIPMultistreamMode': 'On', 
                'Name': 'MRA Traversal to EXPWY-E', 'PeerAddress': ['expe.domain.com'], 
                'AuthenticationMode': 'DoNotCheckCredentials', 
                'SIPPreloadedSipRoutesSupport': 'Off', 'SIPPoisonMode': 'Off', 
                'AcceptProxiedRegistrations': 'Allow', 'SIPParameterPreservationMode': 'Off', 
                'SIPMediaICESupport': 'Off', 'AuthenticationUserName': 'traversal', 
                'HopCount': 15, 'SIPPort': 7001}
            ]
        """
        response = requests.get(self.uc_zone_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response
    
    def createUCTraversalZone(self, json):
        response = requests.post(self.uc_zone_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def updateUCTraversalZone(self, json):
        response = requests.put(self.uc_zone_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def deleteUCTraversalZone(self, zone_name):
        response = requests.put(self.uc_zone_uri, verify=False, auth=(self.exp_user, self.exp_pass), json={"Name":zone_name})
        return response

class ExpEdge(Expressway):
    """
    Child class to define an expressway-e server
    """
    role = "Edge"
    def __init__(self, hostname, username, password):
        super().__init__(hostname, username, password)
        self.traversal_zone_uri = self.base_uri + "/edge/zone/unifiedcommunicationstraversal"
        self.xmpp_uri = self.base_uri + "/edge/xmpp"
    
    def getUCTraversalZone(self) -> list:
        """Returns list of configerud traversal zones.

        Example:
            [
                {'Status': 'Active', 'SIPMediaICESupport': 'Off', 
                'SIPMultistreamMode': 'On', 'Name': 'MRA Traversal to EXPWY-C', 
                'UDPProbeRetryInterval': 2, 'UDPProbeKeepAliveInterval': 20, 
                'SIPPreloadedSipRoutesSupport': 'Off', 
                'SIPTLSVerifySubjectName': 'exp-e.example.com', 
                'AuthenticationMode': 'DoNotCheckCredentials', 'TCPProbeRetryInterval': 2, 
                'SIPPoisonMode': 'Off', 'AcceptProxiedRegistrations': 'Allow', 
                'SIPParameterPreservationMode': 'Off', 'UDPProbeRetryCount': 5, 
                'AuthenticationUserName': 'traversal', 'TCPProbeKeepAliveInterval': 20, 
                'TCPProbeRetryCount': 5, 'HopCount': 15, 'SIPPort': 7001}
            ]
        """
        response = requests.get(self.traversal_zone_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response
    
    def createUCTraversalZone(self, json):
        response = requests.post(self.traversal_zone_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def updateUCTraversalZone(self, json):
        response = requests.put(self.traversal_zone_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response
    
    def deleteUCTraversalZone(self, zone_name):
        response = requests.delete(self.traversal_zone_uri, verify=False, auth=(self.exp_user, self.exp_pass), json={"Name":zone_name})
        return response
    
    def getXMPP(self) -> dict:
        """Returns dictionary of XMPP federation configuration

        Example:
        """
        response = requests.get(self.xmpp_uri, verify=False, auth=(self.exp_user, self.exp_pass)).json()
        return response

    def updateXMPP(self, json):
        response = requests.put(self.xmpp_uri, verify=False, auth=(self.exp_user, self.exp_pass), json=json)
        return response