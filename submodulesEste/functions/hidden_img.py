from stegano import lsb,exifHeader
from PIL import Image
from pathlib import Path

def hidden_img(texto_cifrado, imagen_original, imagen_salida):
    """
    Aqui oculto el texto cifrado cargo la imagen original y luego sale la imagen con el texto cifrado
    :param texto_cifrado:
    :param imagen_original:
    :param imagen_salida:
    :return:
    """
    try:
        extension = imagen_original.split(".")[-1].lower()
        norm_path = Path(imagen_original).resolve()
        ruta_unicode = str(norm_path).encode('utf-8').decode('utf-8')

        img = Image.open(ruta_unicode)

        if extension == "jpg" or extension == "jpeg":
            img_oculta = exifHeader.hide(img,f'uploads/{imagen_salida}',secret_message=texto_cifrado)
        elif extension == "png":
            img_oculta = lsb.hide(img, texto_cifrado)
        else:
            raise ValueError(f"Formato de imagen no compatible: {extension}")

        if img_oculta is not None:
            
            img_oculta.save(f"uploads/{imagen_salida}")
        else:
            print("Ocultación fallida. No se pudo ocultar el texto en la imagen.")

    except Exception as e:
        print(f"Error: {e}")