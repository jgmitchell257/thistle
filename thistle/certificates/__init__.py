from cryptography import x509
from cryptography.hazmat.backends import default_backend
import datetime
import ssl


def download_cert(servername, port=None):
    if port:
        cert = ssl.get_server_certificate((servername, port))
    else:
        cert = ssl.get_server_certificate((servername, 443))
    return cert


def cert_expiration(cert):
    c = x509.load_pem_x509_certificate(cert.encode(), default_backend())
    expires = c.not_valid_after.isoformat()
    return expires
