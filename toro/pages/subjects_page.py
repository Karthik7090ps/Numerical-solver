import flet as ft
from flet import *
import json
from pages.shrink_page import shrink_class
from pages.menu_page import menu_class as menu_class

with open("/home/picchai/Documents/numerical_solver/toso/controls.json", "r") as control_file:
    config = json.load(control_file)

if config["theme"] == 1:
    BG = config["BG"]
    FG = config["FG"]
    FWG = config["FWG"]
    PINK = config["HIGH"]
    TX = config["TX"]
    XT = config["XT"]
elif config["theme"] == 2:
    BG = config["BG1"]
    FG = config["FG1"]
    FWG = config["FWG1"]
    PINK = config["HIGH1"]
    TX = config["TX1"]
    XT = config["XT1"]


class subjects_class(ft.UserControl):
    def __init__(self):
        super().__init__()

    def get_subjects(self):
        subjects_data = config.get("subjects_data", {})
        return list(subjects_data.keys())

    def build(self):
        subjects = self.get_subjects()

        first_data_page = Column(
            width=180
        )
        second_data_page = Column(
            width=195
        )

        midpoint = len(subjects)//2
        first_data=subjects[:midpoint]
        second_data=subjects[midpoint:]


        for subject in first_data:
            first_data_page.controls.append(
            Container(
                border_radius=20,
                bgcolor=FWG,
                width=180,
                height=110,
                padding=15,
                content=Column(
                controls=[
                    Text(subject,color=XT),
                    Container(
                    width=160,
                    height=5,
                    bgcolor='white12',
                    border_radius=20,
                    )
                ]

                )
            )
            )

        for subject in second_data:
            second_data_page.controls.append(
            Container(
                border_radius=20,
                bgcolor=FWG,
                width=185,
                height=110,
                padding=15,
                content=Column(
                controls=[
                    Text(subject,color=XT),
                    Container(
                    width=160,
                    height=5,
                    bgcolor='white12',
                    border_radius=20,
                    )
                ]

                )
            )
            )

        subjects_containers = Column(

            height=600,
            scroll='hidden',
            controls=[
                Row(
                    controls=[
                        first_data_page,Row(
                    height=10,
                    width=1,
                    scroll='ALWAYS'),second_data_page
                    ]
                )
            ]
        )

        subjects_page_incom = Container(
            content=Column(
            controls=[
                Row(alignment='spaceBetween',
                controls=[
                    Container(
                    on_click=lambda e:shrink_class(page_menu=subjects_page),
                    content=Icon(
                        icons.MENU,size=30,color=FWG)),
                    Row(
                    controls=[
                        Container(
                        on_click=lambda _: self.page.go('/'),
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
                Row(
                    height=50
                ),
                Stack(
                controls=[
                    subjects_containers
                ]

                )


            ],
            ),
        )

        subjects_page = Row(alignment='end',
            controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                animate=animation.Animation(600,AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve='decelerate'),
                padding=padding.only(
                top=40,left=5,
                right=5,bottom=5
                ),
                content=Column(
                    controls=[
                    subjects_page_incom
                    ]
                )
            )
            ]
        )

        container=menu_class(page_data_for_menu=subjects_page)

        return container


# def main(page: ft.Page):
#     page.add(subjects_class())


# ft.app(target=main)
