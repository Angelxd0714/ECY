import flet as ft
from menu import menu
from esteganografia import Esteganografia

class body(ft.UserControl):
    """
    Clase que contiene el cuerpo de la aplicacion
    """
    def __init__(self):
        super().__init__()
        self.menu = menu(self)
        self.esteganografia = Esteganografia()
        menu_build = self.menu.build()
        # Usamos una lista en lugar de una tupla
        self.body_content_default: ft.Row = ft.Row([self.menu.build(),ft.VerticalDivider(width=1)], expand=True, height=800)
        self.body_content_tg: ft.Row = ft.Row(
            [
                menu_build,
                ft.VerticalDivider(width=1),
                ft.Column([self.esteganografia], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
        self.body_content_key:ft.Row = ft.Row(
            [
                menu_build,
                ft.VerticalDivider(width=1),
                ft.Column([ft.Text("Keylogger!")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
        self.body_content_ecry:ft.Row =ft.Row(
            [
                menu_build,
                ft.VerticalDivider(width=1),
                ft.Column([ft.Text("Encriptacion!")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    
    def build(self):
        return self.body_content_default

    def update_body_content(self, selected_index=0):
        if selected_index == 0:
            self.body_content_default.controls = self.body_content_tg.controls
        elif selected_index == 1:
            self.body_content_default.controls = self.body_content_key.controls
        elif selected_index == 2:
            self.body_content_default.controls = self.body_content_ecry.controls

        self.update()

