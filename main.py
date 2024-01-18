import flet as ft
from body import body as bd
from submodulesEste.add import Add



def main(page: ft.Page):
    page.title = "ECY"
    page.window_width = 800
    page.window_height = 500
    page.window_maximizable = False
    page.window_max_width = 800
    
    raice = bd() 
    page.add(raice)
    page.overlay.append(raice.esteganografia.box_main.file_picker_dialog_img)
    page.overlay.append(raice.esteganografia.box_main.file_picker_dialog_text)
    page.update() 

ft.app(target=main,upload_dir="uploads")
