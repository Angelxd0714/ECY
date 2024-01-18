import flet as ft

class MenuEstegranoGrafia(ft.UserControl):
    def __init__(self,main):
        super().__init__()
        self.select_index=0
        self.main = main

    def build(self):
        return ft.NavigationBar(
            selected_index=0,
            destinations=[
                ft.NavigationDestination(
                    icon=ft.icons.ADD_CARD, label="Explore"
                ),

                ft.NavigationDestination(
                    icon=ft.icons.BOOKMARK_BORDER,
                    selected_icon=ft.icons.BOOKMARK,
                    label="Explore",
                ),
            ],
            on_change=self.update_box_main,
        )
    def update_box_main(self,e):
        self.select_index = e.control.selected_index
        self.main.update_box_main(self.select_index)        
        self.update()