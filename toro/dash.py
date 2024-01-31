from flet import *

class dash(UserControl):
    def __init__(self):
        super().__init__()
    
    def build(self):
        page_content=Container(
            bgcolor="#E6F4F1",
            height=1080,
            width=1920,
            content=Column(
                controls=[
                Container(
                        height=100,
                        width=1890,
                        bgcolor="#1D818C",
                        content=Row(
                            alignment="spacebetween",
                            controls=[
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
                                )
                            ]
                        ),


                    ),
                
                Column(
                    height=2000,
                    scroll='auto',
                    controls=[
                        Container(
                            height=270,
                            width=1920,
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
                            Row(
                                alignment=MainAxisAlignment.CENTER,
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
                                ]
                            ),
                            ]
                            )

                        ),
                    ]
                )
                ]
            )
        )

        return page_content

def main (page:Page):
    page.add(dash())

app(target=main,assets_dir="assets")