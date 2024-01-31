
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64encode, b64decode
import os
from DB.redis import save_password_redis





def cifrar_texto_cbc(texto, clave)-> bytes:
    """
    tipo de operacion cbc recibe
    dos argumentos texto,clave
    """
    try:
        # Generate a random 16-byte IV for CBC
        iv = os.urandom(16)
        
        # Convert the base64 encoded key to bytes
        mode = "CBC"
        key_bytes = b64decode(clave)[:32]

        # Construct an AES Cipher object with the given key and IV
        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())

        
        encryptor = cipher.encryptor()

        
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        texto_padded = padder.update(texto.encode('utf-8')) + padder.finalize()

       
        ciphertext = encryptor.update(texto_padded) + encryptor.finalize()
        
        save_password_redis(clave,iv,mode)
        return ciphertext
    except Exception as e:
        print(e)
        return None


def cifrar_texto_ofb(texto, clave)-> bytes:
    """
    tipo de operacion ofb recibe
    dos argumentos texto,clave
    """
    try:
        # Generate a random 16-byte IV for CBC
        iv = os.urandom(16)

        # Convert the base64 encoded key to bytes
        mode = "OFB"
        key_bytes = b64decode(clave)[:32]

        # Construct an AES Cipher object with the given key and IV
        cipher = Cipher(algorithms.AES(key_bytes), modes.OFB(iv), backend=default_backend())

        
        encryptor = cipher.encryptor()

        
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        texto_padded = padder.update(texto.encode('utf-8')) + padder.finalize()

       
        ciphertext = encryptor.update(texto_padded) + encryptor.finalize()
        save_password_redis(clave,iv,mode)
        return ciphertext
    except Exception as e:
        print(e)
        return None

def cifrar_texto_ctr(texto, clave)-> bytes:
    """
    tipo de operacion ctr recibe
    dos argumentos texto,clave
    """
    try:
        # Generate a random 16-byte IV for CBC
        iv = os.urandom(16)

        # Convert the base64 encoded key to bytes
        mode = "CTR"
        key_bytes = b64decode(clave)[:32]

        # Construct an AES Cipher object with the given key and IV
        cipher = Cipher(algorithms.AES(key_bytes), modes.CTR(iv), backend=default_backend())

        
        encryptor = cipher.encryptor()

        
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        texto_padded = padder.update(texto.encode('utf-8')) + padder.finalize()

       
        ciphertext = encryptor.update(texto_padded) + encryptor.finalize()
        save_password_redis(clave,iv,mode)
        return ciphertext
    except Exception as e:
        print(e)
        return None




    
