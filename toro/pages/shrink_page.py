from flet import*
import flet as ft

class shrink_class(ft.UserControl):

    def __init__(self,page_menu):
        super().__init__()
        self.menu_page=page_menu
        self.shrink(self)


    def shrink(self,e):
        self.menu_page.controls[0].width = 1
        self.menu_page.controls[0].scale = transform.Scale(
        0,alignment=alignment.center_right)
        self.menu_page.controls[0].border_radius=border_radius.only(
        top_left=35,
        top_right=0,
        bottom_left=35,
        bottom_right=0
        )
        self.menu_page.update()