import flet as ft
from flet import *

BG = '#1b1517'
FG = '#0C1D36'
FWG = '#E5F8F2CB'
PINK = '#F9CC0B'
TX ='#ffffff'
XT ='#000000'

class logo_class(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.image =ft.Image

    def logo(self):

        self.image =ft.Image(
            src="/home/picchai/Documents/numerical_solver/toso/assets/images/logo.png",
            width=200,
            height=200,
            fit=ft.ImageFit.FILL,
            # padding=padding.only(left=10, top=10, bottom=10, right=10)
            repeat=ft.ImageRepeat.NO_REPEAT,
            border_radius=ft.border_radius.all(10))

    def build(self):
        self.logo()
        logo_page_data = Container(
            width=400,
            height=850,
            bgcolor=FG,
            border_radius=35,
            padding=padding.only(left=50,top=60,right=50),

            content=Column(
            controls=[
            Row(
                width=10,
                height=200,
            ),
            Row(alignment='CENTER',
            controls=[
                self.image,
            ]

                )
            ]
            )

        )
        return logo_page_data

# def main(page:ft.Page):
#     page.add(logo_class())

# ft.app(target=main)
