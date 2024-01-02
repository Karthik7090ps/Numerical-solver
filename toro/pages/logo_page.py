import flet as ft
from flet import *
import pages.utility_page as screen_size
import json

with open("/home/picchai/Documents/GItHub/Numerical-solver/toro/controls.json","r") as control_file:
  config = json.load(control_file)

if config["theme"]==1:
    BG      =config["BG"]
    FG      =config["FG"]
    FWG     =config["FWG"]
    PINK    =config["HIGH"]
    TX      =config["TX"]
    XT      =config["XT"]
elif config["theme"]==2:
    BG = config["BG1"]
    FG = config["FG1"]
    FWG = config["FWG1"]
    PINK = config["HIGH1"]
    TX = config["TX1"]
    XT = config["XT1"]

class logo_class(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.image =ft.Image
        self.ws,self.hs,self.W,self.H=screen_size.utility_class.screen_size(self)

    def logo(self):

        self.image =ft.Image(
            src="/home/picchai/Documents/GItHub/Numerical-solver/toro/assets/images/logo.png",
            width=200,
            height=200,
            fit=ft.ImageFit.FILL,
            # padding=padding.only(left=10, top=10, bottom=10, right=10)
            repeat=ft.ImageRepeat.NO_REPEAT,
            border_radius=ft.border_radius.all(10))

    def build(self):
        self.logo()
        logo_page_data = Container(
            width=self.W,
            height=self.H,
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
