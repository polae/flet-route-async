from flet import *
from flet_route import Params, Basket


class Home:
    def __init__(self):
        print(f"{self.__class__.__name__.upper()}.__init__()")

    async def go_to(self, e):
        await self.page.go_async(e.control.data)

    async def view(self, page: Page, params: Params, basket: Basket):
        print(f"-->{self.__class__.__name__.upper()}.view()")
        self.page = page

        return View(
            "/",
            controls=[
                Container(
                    Column(
                        [
                            Row(
                                [
                                    Column(
                                        [
                                            Image(
                                                src="images/home_page.png",
                                                width=256,
                                                border_radius=32,
                                            ),
                                            Text(
                                                "HOME PAGE",
                                                size=36,
                                                font_family="Mont-Regular",
                                            ),
                                            Container(
                                                Text(
                                                    "ABOUT",
                                                    color=colors.AMBER_400,
                                                    font_family="Mont-Regular",
                                                ),
                                                height=24,
                                                width=96,
                                                alignment=alignment.center,
                                                border_radius=16,
                                                border=border.all(
                                                    1, color=colors.AMBER_400
                                                ),
                                                on_click=self.go_to,
                                                data="/about",
                                            ),
                                        ]
                                    )
                                ],
                                alignment=MainAxisAlignment.CENTER,
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    expand=True,
                )
            ],
            bgcolor=colors.BLACK87,  # 2E3440
            scroll=False,
            padding=0,
            spacing=0,
        )
