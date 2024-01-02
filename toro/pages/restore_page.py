from flet import*
import flet as ft
import pages.utility_page as screen_size

class restore_class(ft.UserControl):

    def __init__(self,page_menu):
        super().__init__()
        self.menu_page=page_menu
        self.restore(self)
        self.ws,self.hs,self.W,self.H=screen_size.utility_class.screen_size(self)

    def restore(self,e):
        self.menu_page.controls[0].width = 400
        self.menu_page.controls[0].border_radius = 35
        self.menu_page.controls[0].scale = transform.Scale(

        1,alignment=alignment.center_right)
        self.menu_page.update()