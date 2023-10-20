from flet import *
from flet_route import Params, Basket


class Home:
    def __init__(self):
        print("HOME: __init__()\n")

    async def go_to(self, e):
        await self.page.go_async(e.control.data)

    async def view(self, page: Page, params: Params, basket: Basket):
        print("HOME view() ______________________________________\n\n")
        self.page = page

        return View(
            "/",
            controls=[
                Text("HOME PAGE", size=36),
                Container(
                    Text("ABOUT", color=colors.AMBER_400),
                    height=24,
                    width=96,
                    on_click=self.go_to,
                    data="/about",
                ),
            ],
            bgcolor=colors.GREY_900,
            scroll=False,
            padding=0,
            spacing=0,
        )
