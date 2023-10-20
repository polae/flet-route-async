from flet import *
from flet_route import Params, Basket


class About:
    def __init__(self):
        print("ABOUT: __init__()\n")

    async def go_to(self, e):
        await self.page.go_async(e.control.data)

    async def view(self, page: Page, params: Params, basket: Basket):
        print("ABOUT view() ______________________________________\n\n")
        self.page = page

        return View(
            "/",
            controls=[
                Text("ABOUT PAGE", size=36),
                Container(
                    Text("HOME", color=colors.GREY_600),
                    height=24,
                    width=96,
                    on_click=self.go_to,
                    data="/",
                ),
            ],
            bgcolor=colors.AMBER_700,
            scroll=False,
            padding=0,
            spacing=0,
        )
