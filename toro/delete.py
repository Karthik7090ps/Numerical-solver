from flet import *

class mainpage_class(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        page_data= Container(
            width=400,
            height=850,
            # MainAxisAlignment="centre",
            bgcolor="pink",
            content=(
                Column(
                    controls=[
                        Row(
                            width=400,
                            height=200,
                            controls=[
                            ElevatedButton(text='karthik')
                            ]

                        ),
                        Row(
                            width=400,
                            height=200,
                            controls=[
                                ElevatedButton(text="green Tea")
                            ]
                        )
                    ]
                )
            )
            )
        return page_data
def main(page:Page):
    k=mainpage_class()
    page.add(k)

app(target=main)