from flet import *
from pages.subjects_page import subjects_class

class dash(UserControl):
    def __init__(self):
        super().__init__()
    
    def build(self):
        page_content=ResponsiveRow([
        Container(
            bgcolor="#F2E611",
            height=1080,
            # width=1920,
            content=Column(
                scroll='hidden',
                controls=[
                Container(
                        height=80,
                        # width=1890,
                        bgcolor="#40062D",
                        content=Row(
                            alignment="spacebetween",
                            controls=[
                                Row(width=10),
                                Row(
                                    alignment="spacebetween",
                                    width=900,
                                    controls=[
                                        Text(value="ENGINIFY", size=20, weight="bold"),
                                        Text(value="Community",size=16, weight="regular")
                                        ],
                                ),
                                Row(
                                    width=20,
                                ),
                                Row(
                                    alignment="spacebetween",
                                    width=900,
                                    controls=[
                                        Text(value="About us", size=16, weight="regular"),
                                        Text(value="LOG IN", size=20, weight="semibold")
                                    ]
                                ),
                                Row(width=10),
                            ]
                        ),


                    ),
                
                Column(
                    height=2000,
                    # scroll='always',
                    controls=[
                        Container(
                            height=270,
                            # width=1920,
                            margin=margin.only(top=-10),
                            gradient=LinearGradient(
                                begin=alignment.bottom_right,
                                end=alignment.top_left,
                                colors=[
                                    "#8CE89F",
                                    "#0E87B6",
                                    "#0E87B6",
                                    "#3DA4A9",
                                    "#70C39B",
                                    "#99DC90",
                                    "#BFF386",
                                    "#F9F871"
                                ]
                            ),
                            shadow=BoxShadow(
                                spread_radius=1,
                                blur_radius=15,
                                color=colors.BLUE_GREY_500,
                                offset=Offset(0, 0),
                                blur_style=ShadowBlurStyle.OUTER,
                            ),
                            content=
                            ResponsiveRow(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Column(
                                        controls=[
                                        Stack(
                                            [   
                                                Text(
                                                    spans=[
                                                        TextSpan(
                                                            "ENGINIFY",
                                                            TextStyle(
                                                                size=130,
                                                                weight=FontWeight.BOLD,
                                                                foreground=Paint(
                                                                    color=colors.BLUE_GREY,
                                                                    stroke_width=6,
                                                                    stroke_join=StrokeJoin.ROUND,
                                                                    style=PaintingStyle.STROKE,
                                                                ),
                                                            ),
                                                        ),
                                                    ],
                                                    italic=True,

                                                ),
                                                Text(
                                                    spans=[
                                                        TextSpan(
                                                            "ENGINIFY",
                                                            TextStyle(
                                                                size=130,
                                                                weight=FontWeight.BOLD,
                                                                color=colors.GREY_300,
                                                            ),
                                                        ),
                                                    ],
                                                    italic=True,
                                                ),
                                                Image(
                                                    src="/home/picchai/Documents/GItHub/Numerical-solver/toro/assets/images/img1.png",
                                                    width=1920,
                                                    height=710,
                                                    fit=ImageFit.FIT_WIDTH
                                                ),
                                            ]
                                        ),
                                    ],
                                    alignment=CrossAxisAlignment.CENTER,
                                )

                            ]
                            )
                        ),
                        Container(
                            padding=padding.only(top=30,left=60,right=20),
                            content=(
                                Column(
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        Text(
                                            "What is Enginify?",
                                            theme_style=TextThemeStyle.HEADLINE_SMALL,
                                            color=colors.BLACK87,
                                            weight="bold",
                                            size=36
                                        ),
                                        Text(
                                            "       Welcome to ENGINIFY, your ultimate companion in conquering the complexities of electronics and communication engineering numericals! Engineered with precision and innovation, ENGINIFY is a specialized online toolkit designed to empower engineering students and researchers in seamlessly solving numerical challenges. Dive into a world where theoretical concepts transform into practical solutions, and intricate problems become opportunities for mastery. Our user-friendly interface provides swift access to a plethora of tools crafted to tackle the diverse landscape of numerical problem-solving in the dynamic field of electronics and communication engineering. Unleash your analytical prowess, enhance your understanding, and elevate your academic journey with ENGINIFY - where the power of technology meets the precision of engineering expertise. Embark on a journey of numerical excellence like never before!",
                                            color=colors.BLACK87,
                                            size=22,

                                        ),
                                        Row(height=50),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            controls=[
                                                Container(
                                                    height=70,
                                                    width=250,
                                                    border_radius=border_radius.all(10),
                                                    gradient=LinearGradient(
                                                        colors=[
                                                            "#DE1D08",
                                                            "#40062D"
                                                        ]
                                                    ),
                                                    content=(
                                                        Text("Subjects", size=30,text_align=TextAlign.CENTER,color=colors.WHITE70,weight="bold",italic=True)
                                                    ),
                                                    on_click=lambda e:subjects_class()
                                                ),
                                                Column(width=20),
                                                Container(
                                                    height=70,
                                                    width=250,
                                                    border_radius=border_radius.all(10),
                                                    gradient=LinearGradient(
                                                       colors=[
                                                            "#DE1D08",
                                                            "#40062D"
                                                           
                                                       ]
                                                    ),
                                                    content=(
                                                        Text("Tools", size=30,text_align=TextAlign.CENTER,color=colors.WHITE70,weight="bold",italic=True)
                                                    ),
                                                    on_click=lambda e:subjects_class()
                                                )
                                            ]   
                                        ),
                                        Row(height=50),
                                        Row(
                                            alignment=MainAxisAlignment.CENTER,
                                            controls=[
                                                Column(
                                                    controls=[
                                                Text(
                                                    "Electronics and Communication",
                                                    theme_style=TextThemeStyle.HEADLINE_LARGE,
                                                    color=colors.BLACK87,
                                                    weight="bold",
                                                    size=70,
                                                    italic=True,
                                                    text_align=TextAlign.CENTER
                                                ),
                                                Text(
                                                    "Engineering",
                                                    theme_style=TextThemeStyle.HEADLINE_LARGE,
                                                    color=colors.BLACK87,
                                                    weight="bold",
                                                    italic=True,
                                                    text_align=TextAlign.END,
                                                    size=70,
                                                ),
                                                Row(height=50),
                                                SearchBar(width=1500,bar_bgcolor=colors.BLUE_GREY_50,bar_hint_text="search for subjects or tools"),
                                                    ]
                                                )
                                            ]
                                        ),

                                    ]
                                )
                            )
                        ),
                        Column(
                            alignment=MainAxisAlignment.END,
                            controls=[
                                 Row(height=630),
                                Container(
                                    height=200,
                                    # width=1800,
                                    gradient=LinearGradient(
                                        begin=alignment.top_center,
                                        end=alignment.bottom_center,
                                        colors=[
                                            "#1D818C",
                                            "#73D4A5"
                                        ]
                                    ),
                                    alignment=alignment.top_center,
                                    content=(
                                        Column([
                                        Text("About us", size=30, weight="bold",color=colors.WHITE70),
                                        Text("About us briefly with contacts", size=25, weight="bold",color=colors.WHITE70)
                                        ]
                                        )
                                    )
                                )
                            ]
                        )
                    ]
                )
                ]
            )
        )])

        return page_content

def main (page:Page):
    page.add(dash())

app(target=main)