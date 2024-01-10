import flet as ft
from flet import *
import json
import pages.utility_page as screen_size


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

class profile_class(ft.UserControl):
    def __init__(self,size):
        super().__init__()
        self.circle=None
        self.ws,self.hs,self.W,self.H=screen_size.utility_class.screen_size(self)
        self.size=size*self.hs

    def build(self):
        self.circle = Stack(
            controls=[
                Container(
                        gradient=SweepGradient(
                            center=alignment.center,
                            start_angle=0.0,
                            end_angle=0.0,
                            stops=[0.5,0.5],
                        colors=['#FFFFFFB1', PINK],
                        ),
                        width=100*self.size,
                        height=100*self.size,
                        border_radius=60*self.size,
                        content=Row(alignment='center',
                            controls=[
                                Container(padding=padding.all(5*self.size),
                                bgcolor=BG,
                                width=90*self.size,height=90*self.size,
                                border_radius=50*self.size,
                                content=Container(bgcolor='#FFFFFFB1',
                                    height=80*self.size,width=80*self.size,
                                    border_radius=45*self.size,
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
        return self.circle