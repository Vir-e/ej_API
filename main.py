from typing import Union
from fastapi import FastAPI
from services.books_services import BooksService
from routes import router


app = FastAPI()

app.include_router(router)


