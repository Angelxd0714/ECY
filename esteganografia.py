import flet as ft

from submodulesEste.add import Add
from submodulesEste.extract import Exctract
from submodulesEste.menu import MenuEstegranoGrafia


class Esteganografia(ft.UserControl):
    def __init__(self):
        super().__init__()
        
        # Inicialmente, se instancia la clase 'Add'
     
        self.body = ft.Column()
        self.box_main = Add()
        self.ext_main = Exctract()
        self.menu_main = MenuEstegranoGrafia(self)
         
        self.body_box = ft.Column(
            [
                self.menu_main,
                self.body
                # Se utiliza 'self.box_main.build()' en lugar de 'self.box_main.build(self)'
            ])

    def build(self):
        return self.body_box

    def update_box_main(self, select_index):
        if select_index == 0:
            self.body.controls = [self.box_main]
        elif select_index == 1:
            self.body.controls = [self.ext_main]
        self.update()
