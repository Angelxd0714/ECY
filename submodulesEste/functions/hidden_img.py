from pathlib import Path
from stegano import lsb
from PIL import Image
from pathlib import Path
def hidden_img(texto_cifrado, imagen_original, imagen_salida):
    try:
    # Lee la imagen original con OpenCV
        norm_path = Path(imagen_original).resolve()
        ruta_unicode = str(norm_path).encode('utf-8').decode('utf-8')

        img = Image.open(ruta_unicode)

        # Oculta el texto cifrado en la imagen utilizando LSB
        img_oculta = lsb.hide(img, texto_cifrado)

        # Guarda la imagen resultante
        img_oculta.save(f"{imagen_salida}")
    except:

        return False