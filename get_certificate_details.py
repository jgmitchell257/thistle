import json
import socket
import ssl
"""import OpenSSL




cert_data = ssl.get_server_certificate((hostname, "443"))
cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert_data)
subject = cert.get_subject()
issued_to = subject.CN
issuer = cert.get_issuer()
issued_by = issuer.CN
expires = cert.get_notAfter()

print(f"Issued to: {issued_to}")
print(f"Issued by: {issued_by}")
print(f"Expires: {expires}")"""

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