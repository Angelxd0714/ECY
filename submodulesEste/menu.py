import flet as ft

class MenuEstegranoGrafia(ft.UserControl):
    """
    Menu vertical donde se tiene las distintas microproyectos
    """
    def __init__(self,main):
        super().__init__()
        self.select_index=0
        self.main = main

    def build(self):
        return ft.NavigationBar(
            selected_index=0,
            destinations=[
                ft.NavigationDestination(
                    icon=ft.icons.ADD_CARD, label="EMBED"
                ),

                ft.NavigationDestination(
                    icon=ft.icons.EXPLORE,
                    selected_icon=ft.icons.EXPLORE,
                    label="EXTRACT",
                ),
            ],
            on_change=self.update_box_main,
        )
    def update_box_main(self,e):
        """
        aqui cambio el contenido de la caja principal de acuerdo al menu seleccionado
        :param e: evento de cambio de menu
        :return: None
        """
        self.select_index = e.control.selected_index
        self.main.update_box_main(self.select_index)        
        self.update()