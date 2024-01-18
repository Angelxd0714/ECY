import flet as ft
from .functions.hidden_img import hidden_img as img_hidden
from submodulesEste.functions.password_generate import password_encrypt
from submodulesEste.functions.type_embed import cifrar_texto_cbc


class Add(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.selection_option_cbc = False
        self.selection_option_ofb = False
        self.selection_option_ctr = False
        self.file_picker_dialog_img = ft.FilePicker(
            on_result=self.pick_files_result_img)
        self.file_picker_dialog_text = ft.FilePicker(
            on_result=self.pick_files_result_text)
        self.selected_files_img = ft.TextField(
            label="Seleccione Imagen", read_only=True)
        self.selected_files_text = ft.TextField(
            label="Seleccione Archivo de texto para cifrar", read_only=True,)
        self.password_encrypt = ft.TextField(label="Password", password=True)
        self.name_file = ft.TextField(
            label="Nombrar archivo con respectiva extension", enable_suggestions=True)
        self.content_text = ""
        self.dropdown = ft.Dropdown(
                                options=[
                                    ft.dropdown.Option("CBC"),
                                    ft.dropdown.Option("Green"),
                                    ft.dropdown.Option("Blue"),
                                ],
                                width=100,
                                on_focus=self.select_operation,
                            )

    def pick_files_result_img(self, e: ft.FilePickerResultEvent):
        self.selected_files_img.value = (
            ", ".join(map(lambda f: f.path, e.files)
                      ) if e.files else "Cancelled!"
        )

        self.selected_files_img.update()

    def pick_files_result_text(self, e: ft.FilePickerResultEvent):
        self.selected_files_text.value = (
            ", ".join(map(lambda f: f.name, e.files)
                      ) if e.files else "Cancelled!"
        )
        self.selected_files_text.update()

    def build(self):

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(content=self.selected_files_img, width=500), ft.Container(
                                content=ft.IconButton(icon=ft.icons.UPLOAD_FILE, on_click=lambda _: self.file_picker_dialog_img.pick_files(
                                    allow_multiple=True
                                )))
                        ],

                    ),
                    ft.Row(
                        controls=[
                            ft.Container(content=self.selected_files_text, width=500), ft.Container(
                                content=ft.IconButton(icon=ft.icons.UPLOAD_FILE, on_click=lambda _: self.file_picker_dialog_text.pick_files(allow_multiple=True)))
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Container(content=self.name_file, width=500), ft.Container(
                                content=ft.IconButton(icon=ft.icons.TEXT_FIELDS, on_click=lambda e: print("send")))
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Container(content=self.dropdown
                            ), ft.Container(
                                content=self.password_encrypt)
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Container(content=ft.ElevatedButton(text="Guardar", on_click=lambda e: self.save(
                                e), bgcolor=ft.colors.BLUE_400), width=200)
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

    def open_read_txt(self):
        with open(self.selected_files_text.value, "r") as f:
            while True:
                line = f.readline()
                self.content_text = self.content_text + line + "\n"
                if not line:
                    break
                print(line)

    def embed_cbc(self):
        password = password_encrypt(self.password_encrypt.value)
        key = cifrar_texto_cbc(self.content_text.value, password)
        img_hidden(key, self.selected_files_img.value, self.name_file.value)
        print(self.content_text, self.selected_files_img.value,
              self.selected_files_text.value, password)

    def select_operation(self, e):
        if e.control.value == "CBC":
             self.selection_option_cbc = True
        else:
            print("No selecciono ninguna opcion")

    def save(self, e):
        if self.selection_option_cbc == True:
            self.embed_cbc()
            self.selected_files_text.value = ""
            self.selected_files_img.value = ""
            self.name_file.value = ""
            self.password_encrypt.value = ""
            self.update()
        else:
            print("No selecciono ninguna opcion")
            self.selection_option = False
