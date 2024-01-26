import flet as ft
from body import body as bd
from submodulesEste.add import Add


class Main(ft.Page):
    def __init__(self):
        super().__init__()

    def build(self):
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
        self.update()

if __name__ == "__main__":
    ft.app(target=Main.build, upload_dir="uploads")

