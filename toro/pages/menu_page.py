import flet as ft
from flet import *
import json
from pages.restore_page import restore_class

with open("controls.json","r") as control_file:
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

        def circle_func():
            self.circle = Stack(
                controls=[
                    Container(
                            gradient=SweepGradient(
                                center=alignment.center,
                                start_angle=0.0,
                                end_angle=3,
                                stops=[0.5,0.5],
                            colors=['#00000000', PINK],
                            ),
                            width=100,
                            height=100,
                            border_radius=50,
                            content=Row(alignment='center',
                                controls=[
                                    Container(padding=padding.all(5),
                                    bgcolor=BG,
                                    width=90,height=90,
                                    border_radius=50,
                                    content=Container(bgcolor=FG,
                                        height=80,width=80,
                                        border_radius=40,
                                    content=CircleAvatar(opacity=0.8,
                            foreground_image_url="https://assets.weforum.org/sf_account/image/rA_TF_tkRNKjxk_gzlr9UlBXMhuoPZNeRaRO7-ys_xw.jpg"
                        )
                                    )
                                    )
                                ],
                            ),
                        ),

                ]
            )
        circle_func()


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