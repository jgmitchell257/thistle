import random


def load_word_list() -> list:
    """Load /usr/share/dict/words file

    Returns:
        list: cleaned contents of /usr/share/dict/words
    """
    with open("/usr/share/dict/words", "r") as words:
        word_list = words.readlines()
        cleaned_list = []
        for word in word_list:
            w = word.strip("\n")
            cleaned_list.append(w)
        return cleaned_list


def create_passphrase(x: int) -> str:
    """Create a passphrase that is x words long

    Args:
        x (int): Number of words to sample from the word list

    Returns:
        str: passphrase
    """
    with open("/usr/share/dict/words", "r") as words:
        word_list = words.readlines()
        passphrase_list = random.sample(word_list, k=x)
        random.shuffle(passphrase_list)
        cleaned_list = []
        for word in passphrase_list:
            w = word.strip("\n")
            cleaned_list.append(w)
        return "-".join(cleaned_list)






from cryptography.fernet import Fernet


def create_key() -> bytes:
    """Generate key"""
    key = Fernet.generate_key()
    return key


def load_key(keyfile: str, *args) -> bytes:
    """Loads key from keyfile

    Arguments:
        keyfile (str): name of the file to load

    Returns:
        key (bytes): bytes encoded key
    """
    with open(keyfile, "r") as kf:
        key = kf.read()
    return key.encode()


def save_key(key: bytes, keyfile: str, *args):
    """Saves key to keyfile

    Arguments:
        key (bytes): key in bytes format
        keyfile (str): name of the file to save to

    Returns:
        nothing
    """
    with open(keyfile, "w") as kf:
        kf.write(key.decode())

    return "Success"


def encrypt_string(clr_str: str, key: bytes, *args) -> bytes:
    """Symmetric string encryption

    Arguments:
        clr_str (str): string to be encrypted
        key (bytes): encryption key

    Returns:
        token (bytes): encrypted string
    """
    f = Fernet(key)
    token = f.encrypt(clr_str.encode())
    return token


def decrypt_string(enc_str: bytes, key: bytes, *args) -> str:
    """Symmetric string decryption

    Arguments:
        enc_str (str): string to be decrypted
        key (bytes): encryption key

    Returns:
        token (bytes): decrypted string
    """
    f = Fernet(key)
    token = f.decrypt(enc_str)
    return token.decode()





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
