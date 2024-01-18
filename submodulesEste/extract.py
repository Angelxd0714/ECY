import flet as ft

class Exctract(ft.UserControl):
    def __init__(self):
        super().__init__()
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(content=ft.TextField(label="Cargar Imagen"), width=500), ft.Container(
                                content=ft.IconButton(icon=ft.icons.UPLOAD_FILE, on_click=lambda e: print("send")))
                        ],

                    ),
                    ft.Row(
                        controls=[
                            ft.Container(content=ft.TextField(label="Cargar .txt"), width=500), ft.Container(
                                content=ft.IconButton(icon=ft.icons.UPLOAD_FILE, on_click=lambda e: print("send")))
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.TextField(label="Password", password=True))
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Container(content=ft.ElevatedButton(text="Guardar", on_click=lambda e: print("send"),bgcolor=ft.colors.BLUE_400), width=200)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )



                ]
            ),
            padding=ft.padding.all(30),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            border_radius=ft.border_radius.all(20),
            width=700,
            height=350,
            margin=ft.margin.all(10),
        )