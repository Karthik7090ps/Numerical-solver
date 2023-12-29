import flet as ft
from flet import *
import json
from pages.restore_page import restore_class
from pages.profile_page import profile_class

with open('/home/picchai/Documents/GItHub/Numerical-solver/toro/controls.json','r') as control_file:
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

class menu_class(ft.UserControl):
    def __init__(self,page_data_for_menu):
        super().__init__()
        self.menu_page_data=None
        self.page_data=page_data_for_menu

    def build(self):

        self.circle=profile_class(size=1.5)

        self.menu_page_data = Container(
            width=400,
            height=850,
            bgcolor=BG,
            border_radius=35,
            padding=padding.only(left=50,top=60,right=200),

            content=Column(
            controls=[
            Row(alignment='end',
            controls=[
                Container(border_radius=25,
                padding=padding.only(
                top=13,left=13,),
                height=50,
                width=50,
                border=border.all(color=FWG,width=1),
                on_click=lambda e:restore_class(page_menu=self.page_data),
                content=Text(' >',color=FWG)
                )
                ]
                ),
                Container(height=20),
                self.circle,
                Text('Sundar\nPitchai',size=32,weight='bold',color='white'),
                Container(height=25),
                Row(controls=[
                Icon(icons.FAVORITE_BORDER_SHARP,color='white60'),
                Text('YouTube',size=15,weight=FontWeight.W_300,color='white',font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                Icon(icons.CARD_TRAVEL,color='white60'),
                Text('GitHub',size=15,weight=FontWeight.W_300,color='white',font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                Icon(icons.CALCULATE_OUTLINED,color='white60'),
                Text('LinkedIn',size=15,weight=FontWeight.W_300,color='white',font_family='poppins')
                ]),

                Image(src="/images/1.png",
                width=300,
                height=200,
            ),
            Text('Good',color=FG,font_family='poppins',),
            Text('Consistency',size=21,color='white')

            ]
            )
        )
        self.container = Container(
          width=400,
          height=850,
          bgcolor=BG,
          border_radius=35,
          content=Stack(
            controls=[
              self.menu_page_data,
              self.page_data
            ]

          )

        )
        return self.container