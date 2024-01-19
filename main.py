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
        self.dialog = raice.esteganografia.box_main.dlg
        
        self.add(raice)
        self.overlay.append(raice.esteganografia.box_main.file_picker_dialog_img)
        self.overlay.append(raice.esteganografia.box_main.file_picker_dialog_text)
        self.overlay.append(self.dialog)
        self.update()




ft.app(target=Main.build,upload_dir="uploads")
