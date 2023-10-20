from flet import *
import flet_fastapi
from flet_route import Routing, path

from pages.home import Home
from pages.about import About


async def main(page: Page):
    page.title = "ASYNC TEST"

    app_routes = [
        path(
            url="/",
            clear=True,  # If you want to clear all the routes you have passed so far, then pass True otherwise False.
            view=Home().view,  # Here you have to pass a function or method which will take page,params and basket and return ft.View (If you are using function based view then you just have to give the name of the function.)
        ),
        path(url="/about", clear=True, view=About().view),
    ]

    Routing(
        page=page,  # Here you have to pass the page. Which will be found as a parameter in all your views
        async_is=True,
        app_routes=app_routes,  # Here a list has to be passed in which we have defined app routing like app_routes
    )

    if not page.route:
        page.route = "/"

    await page.go_async(page.route)


app = flet_fastapi.app(main)
