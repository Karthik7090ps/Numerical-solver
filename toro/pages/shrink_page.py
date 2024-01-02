from flet import*
import flet as ft
import pages.utility_page as screen_size

class shrink_class(ft.UserControl):

    def __init__(self,page_menu):
        super().__init__()
        self.menu_page=page_menu
        self.shrink(self)
        self.ws,self.hs,self.W,self.H=screen_size.utility_class.screen_size(self)


    def shrink(self,e):
        self.menu_page.controls[0].width = 0
        self.menu_page.controls[0].scale = transform.Scale(
        1,alignment=alignment.center_right)
        self.menu_page.controls[0].border_radius=border_radius.only(
        top_left=35,
        top_right=0,
        bottom_left=35,
        bottom_right=0
        )
        self.menu_page.update()