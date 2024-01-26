
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives import padding
from stegano import lsb
from stegano import *
from base64 import b64decode
from PIL import Image
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os


def show_message(texto_cifrado, clave, iv=None, mode=None):
    try:
        # Si no se proporciona un IV, generamos uno nuevo
        if mode == "CBC":

            clave = b64decode(clave)[:32]

            # Convierte la clave y el IV de hexadecimal a bytes
            cipher = Cipher(algorithms.AES(clave), modes.CBC(
                iv), backend=default_backend())

            # Crea un objeto de descifrado
            decryptor = cipher.decryptor()

            # Descifra el texto
            decrypted_text = decryptor.update(
                texto_cifrado) + decryptor.finalize()

            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            decrypted_text = unpadder.update(
                decrypted_text) + unpadder.finalize()

            # Devuelve el texto descifrado
            return decrypted_text.decode('utf-8', errors='replace').strip()
        elif mode == "OFB":

            clave = b64decode(clave)

            # Convierte la clave y el IV de hexadecimal a bytes
            cipher = Cipher(algorithms.AES(clave), modes.OFB(
                iv), backend=default_backend())

            # Crea un objeto de descifrado
            decryptor = cipher.decryptor()

            # Descifra el texto
            decrypted_text = decryptor.update(
                texto_cifrado) + decryptor.finalize()

            # Devuelve el texto descifrado
            return decrypted_text.decode('utf-8', errors='replace')
        elif mode == "CTR":
            clave = b64decode(clave)

            # Convierte la clave y el IV de hexadecimal a bytes
            cipher = Cipher(algorithms.AES(clave), modes.OFB(
                iv), backend=default_backend())

            # Crea un objeto de descifrado
            decryptor = cipher.decryptor()

            # Descifra el texto
            decrypted_text = decryptor.update(
                texto_cifrado) + decryptor.finalize()

            # Devuelve el texto descifrado
            return decrypted_text.decode('utf-8', errors='replace')
    except Exception as e:
        print(e)
        return None


def reveal_img(imagen_salida):
    try:
        extension = imagen_salida.split(".")[-1].lower()

        img = Image.open(imagen_salida)

        if extension == "jpg" or extension == "jpeg":
            img_oculta = exifHeader.reveal(img)

        elif extension == "png":
            img_oculta = lsb.reveal(img)
        else:
            raise ValueError(f"Formato de imagen no compatible: {extension}")

        if img_oculta is not None:
            return img_oculta
        else:
            print("Ocultación fallida. No se pudo ocultar el texto en la imagen.")

    except Exception as e:
        print(f"Error: {e}")
