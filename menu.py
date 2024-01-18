import flet as ft


class menu(ft.UserControl):
    def __init__(self, body_instance):
        self._rail = None
        self.body_instance = body_instance
        self.selected_index = 0

    def on_index(self, e):
        self.selected_index = e.control.selected_index
        self.body_instance.update_body_content(self.selected_index)

    def build(self):
        self._rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            # extended=True,
            min_width=100,
            min_extended_width=400,
            #leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.IMAGE_ASPECT_RATIO, 
                    selected_icon=ft.icons.IMAGE_ASPECT_RATIO,
                    label="ESTEGANOGRAFÍA"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.KEY_SHARP,
                    selected_icon=ft.icons.KEY_SHARP,
                    label="Keylogger",
                    
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.ENHANCED_ENCRYPTION,
                    selected_icon=ft.icons.ENHANCED_ENCRYPTION,
                    label="Encriptacion"
                   
                ),
            ],
            on_change=self.on_index,
        )
        return self._rail


# def main(page: ft.Page):

#     rail = ft.NavigationRail(
#         selected_index=0,
#         label_type=ft.NavigationRailLabelType.ALL,
#         # extended=True,
#         min_width=100,
#         min_extended_width=400,
#         leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
#         group_alignment=-0.9,
#         destinations=[
#             ft.NavigationRailDestination(
#                 icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
#             ),
#             ft.NavigationRailDestination(
#                 icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
#                 selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
#                 label="Second",
#             ),
#             ft.NavigationRailDestination(
#                 icon=ft.icons.SETTINGS_OUTLINED,
#                 selected_icon_content=ft.Icon(ft.icons.SETTINGS),
#                 label_content=ft.Text("Settings"),
#             ),
#         ],
#         on_change=lambda e: print("Selected destination:", e.control.selected_index),
#     )

#     page.add(
#         ft.Row(
#             [
#                 rail,
#                 ft.VerticalDivider(width=1),
#                 ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
#             ],
#             expand=True,
#         )
#     )

# ft.app(target=main)
