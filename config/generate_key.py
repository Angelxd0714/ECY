
import configparser
from cryptography.fernet import Fernet


def generate_cipher_key():
    """
    Generates a cipher key for encrypting and decrypting data.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Verificar si la sección 'ENCRYPTION' existe en el archivo de configuración
    if 'ENCRYPTION' not in config:
        # Si no existe, crear la sección 'ENCRYPTION'
        config['ENCRYPTION'] = {}

    # Generar una nueva clave de cifrado
    new_cipher_key = Fernet.generate_key()
    # Convertir la nueva clave a cadena antes de almacenarla en el archivo de configuración
    config['ENCRYPTION']['cipher_key'] = new_cipher_key.decode()

    # Guardar la nueva clave en el archivo de configuración
    with open('config.ini', 'w') as configfile:
        config.write(configfile)



def get_key()->str:
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Obtener el valor de 'cipher_key' como cadena
        cipher_key = config.get('ENCRYPTION', 'cipher_key')
        
        return cipher_key
    except Exception as e:
        print(e)
        return None
   
        
