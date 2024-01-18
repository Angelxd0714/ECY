
import hashlib
from base64 import b64encode, b64decode
import secrets as st
from DB.db import cursor, insert_password
def password_encrypt(password:str)->b64encode:
    """
    El "salt" (salto) es un valor aleatorio que 
    se utiliza en criptografía, especialmente en el 
    contexto de derivación de claves, para añadir entropía 
    y hacer más robusta la seguridad de las contraseñas. 
    Su propósito principal es evitar ataques basados en tablas de arco 
    iris (rainbow tables) y mejorar la seguridad general del almacenamiento y 
    manejo de contraseñas.

    el "key" es la llave donde se utilizar para encriptar 
    la contraseña, es decir, la contraseña encriptada. 
    El algoritmo de encriptación utilizado en esta función es 
    PBKDF2WithHmacSHA256, que es un algoritmo de cifrado 
    basado en derivación de claves utilizado en la criptografía. 
    El algoritmo utilizado para generar la llave es SHA256, 
    que es un algoritmo de cifrado utilizado en la criptografía. 
    El valor de la llave generada es codificado en base64. 

    La función retorna la llave encriptada en base64. 
    """
    salt= st.token_bytes(16)
    print(salt)
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    print(key)
    insert_password(key,salt)
    
    return b64encode(key).decode('utf-8')

















