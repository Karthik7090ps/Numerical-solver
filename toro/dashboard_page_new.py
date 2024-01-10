from flet import *
import math
from pages.shrink_page import shrink_class
from pages.utility_page import utility_class
from pages.profile_page import profile_class as pc

class dashboard_class_new(UserControl):
    def __init__(self):
        super().__init__()
        self.ws,self.hs,self.W,self.H=utility_class.screen_size(self)

    def build(self):
        page_details=Container(
            bgcolor=colors.WHITE,
            border_radius=25,
            height=self.H,
            width=self.W,
            padding=padding.only(
                top=30,bottom=50,
                right=0,left=0,
            ),
            content=(
                Column(
                    controls=[
                        Container(
                            gradient=LinearGradient(
                                begin=alignment.top_left,
                                end=Alignment(0.8, 1),
                                colors=[
                                    "#2582E0",
                                    "#000000",
                                ],
                                tile_mode=GradientTileMode.MIRROR,
                                rotation=math.pi / 3,
                            ),
                            width=self.W,
                            height=self.H*0.15,
                            margin=margin.all(-5),
                            content=(
                                Row(
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            height=self.H*0.1,
                                            width=self.W/15,
                                            # bgcolor='red',
                                            on_click=lambda e:shrink_class(page_menu=page_details),
                                            content=(
                                                Container(
                                                    pc(0.9),
                                                )
                                            )
                                        ),
                                        Container(
                                            height=self.H*0.10,
                                            width=self.W/7,
                                            # bgcolor='yellow',
                                            content=(
                                                Column(
                                                    alignment='start',
                                                    height=self.H*0.7,
                                                    width=self.W,
                                                    controls=[
                                                        Row(
                                                            alignment=MainAxisAlignment.CENTER,
                                                            height=self.H*0.05,
                                                            width=self.W,
                                                            controls=[
                                                                Text(value='  ENGINIFY',color='white',weight='w900',size=30,text_align=TextAlign.CENTER),
                                                            ]
                                                        ),
                                                        Row(
                                                            alignment=MainAxisAlignment.CENTER,
                                                            height=self.H*0.03,
                                                            controls=[
                                                                Text(value='INPUT TO OUTPUT',color='white',weight='w900',size=20,text_align=TextAlign.CENTER),
                                                            ]
                                                        ),
                                                    ]
                                                )
                                            )
                                        )
                                    ]
                                )
                            )
                        ),
                        Container(
                            # alignment=alignment.center,
                            gradient=LinearGradient(
                                begin=alignment.top_left,
                                end=Alignment(0, 1),
                                colors=[
                                    "#000000",
                                    "#027CBD",
                                ],
                                tile_mode=GradientTileMode.MIRROR,
                                rotation=math.pi / 3,
                            ),
                            width=self.W,
                            height=self.H*0.8,
                            margin=margin.all(-5),
                            content=(
                                Row(
                                    width=10,
                                    height=20,
                                    controls=[
                                        ElevatedButton(text='karthik',)
                                    ]
                                )


                            )
                        )

                    ]
                )
                )
            )
        return page_details

def main(page:Page):
    page.add(dashboard_class_new())
app(target=main)