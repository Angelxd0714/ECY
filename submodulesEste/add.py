import flet as ft

from DB.redis import save_password_redis
from config.generate_key import generate_cipher_key
from .functions.hidden_img import hidden_img as img_hidden
from submodulesEste.functions.password_generate import password_encrypt
from submodulesEste.functions.type_embed import cifrar_texto_cbc, cifrar_texto_ctr, cifrar_texto_ofb


class Add(ft.UserControl):
    """
    Aqui obtengo la url de imagen, el texto que quiero cifrar y la contraseña con la que se va a guardar
    """
    def __init__(self):
        super().__init__()

        self.selection_option_cbc = False
        self.selection_option_ofb = False
        self.selection_option_ctr = False
        self.text_alert = ""
        self.dlg = ft.AlertDialog(
            title=ft.Text(self.text_alert), on_dismiss=lambda e: print("Dialog dismissed!")
        )

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
                ft.dropdown.Option("OFB"),
                ft.dropdown.Option("CTR"),
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
                                content=ft.Icon(name=ft.icons.EXTENSION),margin=7)
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
                                e), bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE), width=200)
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
        """
        aqui leo el archivo de texto y lo guardo en una variable para poder cifrarlo
        :return:
        
        """
        with open(self.selected_files_text.value, "r") as f:
            while True:
                line = f.readline()
                self.content_text = self.content_text + line + "\n"
                if not line:
                    break

    def embed_cbc(self):
        """
        aqui genero la llave para cada operacion en este caso cbc y guardarlo en .ini para la contraseña y trigo la operacion de type_embed.py 
        """
        try: 
            generate_cipher_key()
           
            password = password_encrypt(self.password_encrypt.value)
          
            self.open_read_txt()
        
            key = cifrar_texto_cbc(self.content_text, password)
            
            img_hidden(key, self.selected_files_img.value, self.name_file.value)
        except Exception as e:
            print(e)
    
            return None
        

    def embed_ofb(self):
        """
        aqui genero la llave para cada operacion en este caso ofb y guardarlo en .ini para la contraseña y trigo la operacion de type_embed.py 
        """
        generate_cipher_key()
        password = password_encrypt(self.password_encrypt.value)
        self.open_read_txt()
        key = cifrar_texto_ofb(self.content_text, password)
        img_hidden(key, self.selected_files_img.value, self.name_file.value)
      

    def embed_ctr(self):
        """
        aqui genero la llave para cada operacion en este caso ctr y guardarlo en .ini para la contraseña y trigo la operacion de type_embed.py 
        """
        generate_cipher_key()
        password = password_encrypt(self.password_encrypt.value)
        self.open_read_txt()
        key = cifrar_texto_ctr(self.content_text, password)
        img_hidden(key, self.selected_files_img.value, self.name_file.value)
     

    def select_operation(self, e):
        """
        selecciona la operacion a realizar
        :param e:
        :return:
        """
        if e.control.value == "CBC":
            self.selection_option_cbc = True
        elif e.control.value == "OFB":
            self.selection_option_ofb = True
        elif e.control.value == "CTR":
            self.selection_option_ctr = True
        else:
            print("No selecciono ninguna opcion")

    def open_alert(self, e, text):
        """
        genera un alert cuando completa una operacion o hay un error
        """
        self.text_alert = text
        self.dlg.title = ft.Text(self.text_alert)
        self.dlg.open = True
        self.dlg.update()

    def save(self, e):
        """
        aqui dependiendo de la seleccion hara una operacion distinta
        
        """
        if self.selection_option_cbc == True:
            try:
                self.embed_cbc()
                self.selected_files_text.value = ""
                self.selected_files_img.value = ""
                self.name_file.value = ""
                self.password_encrypt.value = ""
              
                self.open_alert(e, "Se oculto la imagen")
                self.update()
               
            except Exception as f:
                self.open_alert(e, "hubo un error")
                
        elif self.selection_option_ofb == True:
            self.embed_ofb()
            self.selected_files_text.value = ""
            self.selected_files_img.value = ""
            self.name_file.value = ""
            self.password_encrypt.value = ""

            self.open_alert(e,"Se oculto la imagen")
            self.update()
        elif self.selection_option_ctr == True:
            self.embed_ctr()
            self.selected_files_text.value = ""
            self.selected_files_img.value = ""
            self.name_file.value = ""
            self.password_encrypt.value = ""

            self.open_alert(e,"Se oculto la imagen")
            self.update()
        else:
            print("No selecciono ninguna opcion")
            self.selection_option_cbc = False
            self.selection_option_ofb = False
            self.selection_option_ctr = False
