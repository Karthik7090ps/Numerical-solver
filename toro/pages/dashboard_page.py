import flet as ft
from flet import *
import random
import json
from pages.shrink_page import shrink_class
from pages.menu_page import menu_class as menu_class
from pages.profile_page import profile_class
import pages.utility_page as screen_size


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


class dashboard_class(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.ws,self.hs,self.W,self.H=screen_size.utility_class.screen_size(self)


    def build(self):
        Page.padding=0

        subjects = Column(
            height=340*self.ws,
            scroll='always',
        )

        def subjects_names():
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
            return electronics_subjects

        for subject in subjects_names():
            subjects.controls.append(Row(
                controls=[
                    Container(
                        on_click=lambda _: self.page.go('/dashboard/subjects/subject'),
                        content=
                        ElevatedButton(height=70*self.hs,width=350*self.ws,text=subject,color=XT),)
                    ]
                )
            )

        categories_card = Row(
            scroll='auto'
        )

        categories = ['ECE','CSE','EEE','MECH']

        for i, category in enumerate(categories):
            k = random.randint(20,40)
            categories_card.controls.append(
            Container(
                border_radius=20,
                bgcolor=FWG,
                width=170   *self.ws,
                height=110  *self.hs,
                padding=15,
                content=Column(
                controls=[
                    Text(value=f'{k} Subjects', color=XT),
                    Text(category,color=XT),
                    Container(
                    width=160*self.ws,
                    height=5*self.hs,
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

        avathar=profile_class(size=1)

        anchor = ft.SearchBar(
            height=45,
            width=230,
                            view_elevation=2,
                            divider_color=ft.colors.DEEP_PURPLE_ACCENT,
                            bar_hint_text="Search Topics...",
                            bar_bgcolor='#FFFFFFA6',
                            view_hint_text="Choose a color from the suggestions...",

                            controls=[
                                ft.ListTile(title=ft.Text(f"Color {i}"), on_click=None, data=i)
                                for i in range(10)
                            ],
                        )

        first_page_contents = Container(
            content=Column(
            controls=[
                Row(alignment='spaceBetween',
                controls=[
                    Container(
                    on_click=lambda e:shrink_class(page_menu=dashboard_page),
                    content=Container(
                        avathar,animate_size=30
                    )),
                    Container(padding=0,
                        content=Column(
                            controls=[
                                Text(value="  ENGIFY",size=20*self.ws,width=200*self.ws,color='white',text_align=TextAlign.CENTER,
                                     ),
                                Text(value=" Input to output",size=15*self.ws,width=200*self.ws,color='white',text_align=TextAlign.CENTER,
                                     ),
                                anchor,
                            ]
                        ),
                    ),

                    Row(
                    controls=[
                        Container(
                        on_click=lambda _: self.page.go('/dashboard/subjects'),
                        content=Icon(
                        icons.NOTIFICATIONS,size=45*self.hs,color=FWG))
                    ],
                    ),
                ],
                ),
                Container(height=20*self.hs),
                Text(
                value='What\'s up, Sundar!',color=TX
                ),
                Text(
                value='CATEGORIES',color=TX
                ),
                Container(
                padding=padding.only(top=10*self.hs,bottom=20*self.hs,),
                content=categories_card
                ),
                Container(height=5*self.hs),
                Text("SUBJECTS",color=TX),
                Stack(
                controls=[
                    subjects
                ]
                )
            ],
            ),
        )

        dashboard_page = Row(alignment='end',
            controls=[
            Container(
                width=self.W,
                height=self.H,
                bgcolor=FG,
                border_radius=35,
                animate=animation.Animation(600,AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve='decelerate'),
                padding=padding.only(
                top=25,left=20,
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