import ssl
import OpenSSL


hostname =  input("Enter hostname (www.example.com) to check > ")

cert_data = ssl.get_server_certificate((hostname, "443"))
cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert_data)
subject = cert.get_subject()
issued_to = subject.CN
issuer = cert.get_issuer()
issued_by = issuer.CN
expires = cert.get_notAfter()

print(f"Issued to: {issued_to}")
print(f"Issued by: {issued_by}")
print(f"Expires: {expires}")
