
import flet as ft
from DB.redis import get_password_salt
from submodulesEste.functions.show_message_img import  reveal_img, show_message

class Exctract(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.text_alert = ""
        self.dlg = ft.AlertDialog(
            title=ft.Text(self.text_alert), on_dismiss=lambda e: print("Dialog dismissed!")
        )
        self.file_picker_dialog_img = ft.FilePicker(
            on_result=self.pick_files_result_img)
        self.selected_files_img = ft.TextField(
            label="Seleccione Imagen", read_only=True)
        self.selected_files_text = ft.TextField(
            label="contenido",multiline=True,read_only=True)
        self.password_encrypt = ft.TextField(label="Password", password=True)
        self.name_file = ft.TextField(
            label="Nombrar archivo con respectiva extension", enable_suggestions=True)
        
    def pick_files_result_img(self, e: ft.FilePickerResultEvent):
        self.selected_files_img.value = (
            ", ".join(map(lambda f: f.path, e.files)
                      ) if e.files else "Cancelled!"
        )

        self.selected_files_img.update()

    def pick_files_result_text(self, e: ft.FilePickerResultEvent):
        self.selected_files_text.value = (
            ", ".join(map(lambda f: f.path, e.files)
                      ) if e.files else "Cancelled!"
        )
        self.selected_files_text.update()
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(content= self.selected_files_img, width=500), ft.Container(
                                content=ft.IconButton(icon=ft.icons.UPLOAD_FILE, on_click=lambda _:self.file_picker_dialog_img.pick_files(
                                    allow_multiple=True
                                )))
                        ],

                    ),
                    ft.Row(
                        controls=[
                            ft.Container(content=self.selected_files_text, width=500), ft.Container(
                                content=ft.Icon(name=ft.icons.EXTENSION),margin=7)
                        ],height=100
                    ),
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=self.password_encrypt)
                        ]
                    ),
                    
                    ft.Row(
                        controls=[
                            ft.Container(content=ft.ElevatedButton(text="Mostrar", on_click=lambda e: self.extract(e),bgcolor=ft.colors.BLUE_400,color=ft.colors.WHITE), width=200)
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
    def extract(self, e):
        try:
            result = get_password_salt(self.password_encrypt.value)
            if result:
                key, vi, mode = result      
                img = reveal_img(self.selected_files_img.value)
                show = show_message(img, key, vi, mode)
                self.selected_files_text.value = show
                self.selected_files_text.update()
            else:
                print("No se pudo obtener la contraseña.")
        except Exception as ex:
            print(f"Error en extract: {ex}")