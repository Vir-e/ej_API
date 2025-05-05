from pydantic import BaseModel, StrictStr, StrictFloat
from datetime import date

class BookDTO(BaseModel):
    title: StrictStr
    author: StrictStr
    publication_date: date
    price: StrictFloat


