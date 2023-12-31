from flet import *
import flet as ft
import time
from pages.dashboard_page import dashboard_class
from pages.logo_page import logo_class
from pages.subjects_page import subjects_class
from pages.menu_page import menu_class as menu_class
import json

with open("/home/picchai/Documents/numerical_solver/toso/controls.json","r") as control_file:
  config = json.load(control_file)

def main(page: Page):

  pages_v = {
      '/':View(
                "/",
                [
                   logo_class()
                ],
            ),
      '/dashboard':View(
              "/dashboard",
              [
                dashboard_class()
              ]
      ),
      '/dashboard/subjects':View(
        "/dashboard/subjects",
        [
          subjects_class()
        ]
      )
      # '/create_task': View(
      #               "/create_task",
      #               [
      #                   create_task_view
      #               ],
      #           )

    }

  def route_change(route):
    page.views.clear()
    page.views.append(
    pages_v[page.route]
    )
    if page.route =="/":
      page.update()
      time.sleep(3)
      page.go("/dashboard")




  page.on_route_change = route_change
  page.go(page.route)



app(target=main,assets_dir='assets', port=5000)