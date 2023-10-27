from pydantic import BaseModel
from typing import Optional


class Quotation(BaseModel):
    quote: str
    author: str
    category: Optional[str] = None

    def __str__(self):
        return f'"{self.quote}" \n\t--{self.author}'
