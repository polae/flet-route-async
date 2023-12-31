from flet import *
from flet_route import Params, Basket

from packages.api import GetQuote
from packages.controls import LinkButton, DisplayQuotation, PolaeMarkdown
from packages.schemas import Quotation
from packages.styles import COLORS


class Home:
    def __init__(self):
        print(f"{self.__class__.__name__.upper()}.__init__()")

    async def view(self, page: Page, params: Params, basket: Basket):
        print(f"-->{self.__class__.__name__.upper()}.view()")
        self.page = page

        self.quote: Quotation = await GetQuote()
        basket.quote: Quotation = self.quote

        self.display_quotation = DisplayQuotation(self.quote)
        self.about_button = LinkButton("ABOUT", "/about")

        self.screen = Container(
            Column(
                [
                    Text(
                        "This quotation is a response from from the API.",
                        size=24,
                        color=COLORS["text"],
                        font_family="Mont-Semi-Bold",
                    ),
                    self.display_quotation,
                    self.about_button,
                ],
                width=512,
                alignment=MainAxisAlignment.CENTER,
            ),
            bgcolor=COLORS["background"],
            alignment=alignment.center,
            expand=True,
        )

        return View(
            "/",
            controls=[self.screen],
            bgcolor=COLORS["background"],
            scroll=False,
            padding=0,
            spacing=0,
        )
