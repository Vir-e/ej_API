from pydantic import BaseModel
from datetime import date

class BookDTO(BaseModel):
    title: str
    author: str
    publication_date: date
    price: float


