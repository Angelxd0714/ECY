import flet as ft
from body import body as bd
from submodulesEste.add import Add
from submodulesEste.functions.file import create_directory


class Main(ft.Page):
    """
    Aqui se crea la ventana principal de la aplicacion.
    """
    def __init__(self):
        super().__init__()

    def build(self):
        """
        Construye la ventana principal de la aplicacion.
        :return: None.
        """
        self.title = "ECY"
        self.window_width = 800
        self.window_height = 500
        self.window_maximizable = False
        self.window_max_width = 800
        raice = bd()

        self.dialog_main_add = raice.esteganografia.box_main.dlg
        self.dialog_ext = raice.esteganografia.ext_main.dlg
        self.add(raice)
        self.overlay.append(
            raice.esteganografia.box_main.file_picker_dialog_img)
        self.overlay.append(
            raice.esteganografia.box_main.file_picker_dialog_text)
        self.overlay.append(self.dialog_main_add)
        self.overlay.append(
            raice.esteganografia.ext_main.file_picker_dialog_img)
        self.overlay.append(self.dialog_ext)
        create_directory()
        self.update()

if __name__ == "__main__":
    ft.app(target=Main.build, upload_dir="uploads")

