from flet import *
from flet_route import Params, Basket

from packages.api import GetQuote
from packages.controls import LinkButton, DisplayQuotation
from packages.schemas import Quotation
from packages.styles import COLORS


class About:
    def __init__(self):
        print(f"{self.__class__.__name__.upper()}.__init__()")

    async def view(self, page: Page, params: Params, basket: Basket):
        print(f"-->{self.__class__.__name__.upper()}.view()")
        self.page = page

        if not hasattr(basket, "quote"):
            self.quote = Quotation(author="No author", quote="No quotation")
        else:
            self.quote = basket.quote

        # ALTERNATE SYNTAX
        # if basket.get("quote") is not None:
        #     self.quote = basket.quote
        # else:
        #     self.quote = Quotation(author="No author", quote="No quotation")

        self.display_quotation = DisplayQuotation(self.quote)
        self.home_button = LinkButton("HOME", "/")

        self.screen = Container(
            Column(
                [
                    Text(
                        "This quotation was passed through the BASKET.",
                        size=24,
                        color=COLORS["text"],
                        font_family="Mont-Semi-Bold",
                    ),
                    self.display_quotation,
                    self.home_button,
                ],
                width=512,
                alignment=MainAxisAlignment.CENTER,
            ),
            bgcolor=COLORS["background"],
            alignment=alignment.center,
            expand=True,
        )

        return View(
            "/about",
            controls=[self.screen],
            bgcolor=COLORS["background"],
            scroll=False,
            padding=0,
            spacing=0,
        )
