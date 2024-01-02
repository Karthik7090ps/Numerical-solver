import screeninfo
import flet as ft
from flet import *

class utility_class (ft.UserControl):
    def __init__(self):
        super().__init__()
        self.screen_size()


    def screen_size(self):
        self.wed=400
        self.het=850
        monitors = screeninfo.get_monitors()
        for i, monitor in enumerate(monitors, 1):

            # Optionally, if you want to return the size of the primary screen
            if i == 1:  # Assuming primary screen is the first in the list
                width_scale=round(monitor.width/400,2)
                height_scale=round(monitor.height/850,2)
                print(f"Screen {i} - Width: {monitor.width}, Height: {monitor.height},height: {height_scale}, width: {width_scale}")
                return width_scale, height_scale, monitor.width, monitor.height
                # return self.wed,self.het

# Creating an instance of the class
util = utility_class()
