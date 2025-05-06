from pydantic import BaseModel, StrictStr, StrictFloat
from datetime import date

# El DTO actúa además como objeto de dominio, en proyectos más grandes se implementaría un objeto de dominio separado que se usaría para la lógica de negocio
class BookDTO(BaseModel):
    title: StrictStr
    author: StrictStr
    publication_date: date
    price: StrictFloat


