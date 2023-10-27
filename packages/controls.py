from flet import *

from packages.schemas import Quotation
from packages.styles import COLORS


class LinkButton(UserControl):
    def __init__(self, text, link):
        super().__init__()
        self.text: str = text
        self.link: str = link

    async def go_to(self, e):
        await self.page.go_async(self.link)

    def build(self):
        return Container(
            Text(
                f"{self.text.upper()}",
                size=20,
                color=COLORS["warning"],
                font_family="Mont-Regular",
            ),
            height=32,
            width=128,
            alignment=alignment.center,
            border_radius=16,
            border=border.all(1, color=COLORS["warning"]),
            on_click=self.go_to,
            data=f"{self.link}",
        )


class DisplayQuotation(UserControl):
    def __init__(self, quote: Quotation):
        super().__init__()
        self.quote: Quotation = quote

    def build(self):
        return Container(
            Column(
                [
                    Text(
                        self.quote.author,
                        size=24,
                        color=COLORS["warning"],
                        font_family="Mont-Semi-Bold",
                    ),
                    Text(
                        self.quote.quote,
                        size=24,
                        color=COLORS["foreground"],
                        font_family="Mont-Regular",
                    ),
                ],
                # width=512,
            )
        )


class PolaeMarkdown(UserControl):
    def __init__(self, text: str):
        super().__init__()
        self.text = text

    def build(self):
        return Markdown(
            value=self.text,
            extension_set="gitHubWeb",
            code_theme="nord",
            scale=1.2,
            code_style=TextStyle(font_family="Fira-Retina", size=20),
            selectable=True,
        )
