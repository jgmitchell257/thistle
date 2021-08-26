"""
pytools.keys
~~~~~~~~~~~~
Simple module for encryption tools
"""

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
