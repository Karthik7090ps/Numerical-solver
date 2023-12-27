import flet as ft
from flet import *
import random
import json
from pages.shrink_page import shrink_class
from pages.menu_page import menu_class as menu_class

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


class dashboard_class(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):

        subjects = Column(
            height=400,
            scroll='auto',
        ) 

        electronics_subjects = [
            "Analog Electronics",
            "Digital Signal Processing",
            "Control Systems",
            "Microelectronics",
            "Electronic Circuits",
            "Communication Systems",
            "VLSI Design",
            "Embedded Systems",
            "Electromagnetic Fields",
            "Power Electronics"
        ]

        for subject in electronics_subjects:
            subjects.controls.append(
                Container(
                    height=70,
                    width=400,
                    bgcolor=FWG,
                    border_radius=25,
                    padding=padding.only(left=20, top=25),
                    content=Container(
                        Text(value=subject,color=XT)
                    )
                ),
            )

        categories_card = Row(
            scroll='hidden'
        )

        categories = ['ECE','CSE','EEE','MECH']

        for i, category in enumerate(categories):
            k = random.randint(20,40)
            categories_card.controls.append(
            Container(
                border_radius=20,
                bgcolor=FWG,
                width=170,
                height=110,
                padding=15,
                content=Column(
                controls=[
                    Text(value=f'{k} Subjects', color=XT),
                    Text(category,color=XT),
                    Container(
                    width=160,
                    height=5,
                    bgcolor='white12',
                    border_radius=20,
                    padding=padding.only(right=i*30),
                    content=Container(
                        bgcolor=PINK,
                    ),
                    )
                ]

                )
            )
            )

        first_page_contents = Container(
            content=Column(
            controls=[
                Row(alignment='spaceBetween',
                controls=[
                    Container(
                    on_click=lambda e:shrink_class(page_menu=dashboard_page),
                    content=Icon(
                        icons.MENU,size=30,color=FWG)),
                    Row(
                    controls=[
                        Container(
                        on_click=lambda _: self.page.go('/dashboard/subjects'),
                        content=Icon(
                        icons.NOTIFICATIONS,size=30,color=FWG))
                    ],
                    ),
                ],
                ),
                Container(height=20),
                Text(
                value='What\'s up, Sundar!',color=TX
                ),
                Text(
                value='CATEGORIES',color=TX
                ),
                Container(
                padding=padding.only(top=10,bottom=20,),
                content=categories_card
                ),
                Container(height=5),
                Text("SUBJECTS",color=TX),
                Stack(
                controls=[
                    subjects,Row(
                    height=10,
                    width=5,
                    scroll='ALWAYS')
                ]
                )
            ],
            ),
        )

        dashboard_page = Row(alignment='end',
            controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                animate=animation.Animation(600,AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve='decelerate'),
                padding=padding.only(
                top=50,left=20,
                right=20,bottom=5
                ),
                content=Column(
                    controls=[
                    first_page_contents
                    ]
                )
            )
            ]
        )

        final_page = menu_class(page_data_for_menu=dashboard_page)
        
        return final_page

# def main(page:ft.Page):
#     page.add(dashboard_class())

# ft.app(target=main)