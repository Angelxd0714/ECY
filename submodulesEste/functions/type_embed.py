
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64encode, b64decode
import secrets
def cifrar_texto_cbc(texto, clave):
    try:
        iv = b64encode(secrets.token_bytes(16)).decode('utf-8')
        # Crea un objeto Cipher para AES en modo CBC
        cipher = Cipher(algorithms.AES(b64decode(clave)), modes.CBC(b64decode(iv)), backend=default_backend())

        # Crea un objeto de cifrado
        encryptor = cipher.encryptor()

        # Aplica el padding al texto
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        texto_padding = padder.update(texto.encode('utf-8')) + padder.finalize()

        # Cifra el texto
        ciphertext = encryptor.update(texto_padding) + encryptor.finalize()

        # Devuelve el ciphertext como base64
        return b64encode(ciphertext).decode('utf-8')
    except Exception as e:
        print(e)
        return None


def cifrar_texto_ofb(texto, clave):
    try:
        iv = b64encode(secrets.token_bytes(16)).decode('utf-8')
        # Crea un objeto Cipher para AES en modo CBC
        cipher = Cipher(algorithms.AES(b64decode(clave)), modes.OFB(b64decode(iv)), backend=default_backend())

        # Crea un objeto de cifrado
        encryptor = cipher.encryptor()

        # Aplica el padding al texto
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        texto_padding = padder.update(texto.encode('utf-8')) + padder.finalize()

        # Cifra el texto
        ciphertext = encryptor.update(texto_padding) + encryptor.finalize()

        # Devuelve el ciphertext como base64
        return b64encode(ciphertext).decode('utf-8')
    except Exception as e:
        print(e)
        return None

def cifrar_texto_ctr(texto, clave):
    try:
        iv = b64encode(secrets.token_bytes(16)).decode('utf-8')
        # Crea un objeto Cipher para AES en modo CBC
        cipher = Cipher(algorithms.AES(b64decode(clave)), modes.CTR(b64decode(iv)), backend=default_backend())

        # Crea un objeto de cifrado
        encryptor = cipher.encryptor()

        # Aplica el padding al texto
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        texto_padding = padder.update(texto.encode('utf-8')) + padder.finalize()

        # Cifra el texto
        ciphertext = encryptor.update(texto_padding) + encryptor.finalize()

        # Devuelve el ciphertext como base64
        return b64encode(ciphertext).decode('utf-8')
    except Exception as e:
        print(e)
        return None