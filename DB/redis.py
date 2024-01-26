import redis
from base64 import b64encode, b64decode
import hashlib
import json
import base64
import secrets
from cryptography.fernet import Fernet
import configparser

from config.generate_key import get_key

connect_r = redis.Redis(host='localhost', port=6379, db=0)


def save_password_redis(password, vi, mode):
    try:

        vi_base64 = base64.b64encode(vi).decode('utf-8')

        # Crear un diccionario con las representaciones en base64
        current_data = {"vi": vi_base64, "mode": mode}

        # Convertir el diccionario a una cadena JSON
        json_data = json.dumps(current_data)

        # Almacenar el valor en Redis con la clave siendo la contraseña
        connect_r.set(password, json_data)
    except Exception as e:
        print(e)


def get_password_salt(password):
    try:
        # Obtener todas las claves
        keys = connect_r.keys()
        for key in keys:
            get_key_password = get_key()

            descriptar = Fernet(get_key_password)

            # Convertir la clave a bytes antes de descifrar
            key_bytes = key

            valor_final = descriptar.decrypt(key_bytes).decode()

            if valor_final == password:
                # Obtener el valor de la clave
                value = connect_r.get(key)
                # Convertir el valor a un diccionario
                data = json.loads(value)
                # Obtener el valor de la clave vi
                vi = data["vi"]
                # Decodificar el valor de vi
                vi_bytes = base64.b64decode(vi)

                mode = data["mode"]

                return key, vi_bytes, mode
            else:
                return False

    except Exception as e:
        print("Error en get_password_salt:", repr(e))
        return False
