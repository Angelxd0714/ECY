
import hashlib
from base64 import b64encode, b64decode
import secrets as st
from cryptography.fernet import Fernet
import configparser

from config.generate_key import get_key
def password_encrypt(password):
    """
    
    """
    try:
        key =  get_key()
        fernet = Fernet(key)
        encrypted_password = fernet.encrypt(password.encode('utf-8'))
        return encrypted_password
    except Exception as e:
        print(e)
        return None






    
    
















