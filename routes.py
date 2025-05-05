from fastapi import APIRouter, Depends, HTTPException
from typing import Union
from models.book_DTO import BookDTO
from sqlalchemy.orm import Session
from utils.dependencies import get_db
from services.books_services import BooksService
from typing import List

router = APIRouter()



@router.get("/books/", response_model=List[BookDTO])
def get_books(db: Session = Depends(get_db)):
    book_service = BooksService()
    books = book_service.get_books(db)
    return books




@router.get("/books/{book_id}", response_model=BookDTO)
def get_book(book_id: int, Session = Depends(get_db)):
    book_service = BooksService()
    book = book_service.get_book(book_id, Session)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/books/")
def create_book(book_data: BookDTO, db: Session = Depends(get_db)):
    book_service = BooksService()
    book_create = book_service.create_book(book_data, db)
    if book_create is None:
        raise HTTPException(status_code=400, detail="Book creation failed")
    return book_create

# TODO SEGUIR REPASANDO FLUJO DESDE AQUI, CONTROLANDO EXCEPCIONES Y RESPUESTAS
# TODO IMPLEMENTAR LOGIN Y MIRAR AUTENTICACIÓN Y AUTORIZACIÓN CON CONTRASEÑAS
# TODO PAGINACION EN EL GET LIBROS

@router.put("/books/{book_id}")
def update_book(book_id: int, book_data: BookDTO, db: Session = Depends(get_db)):
    book_service = BooksService()
    book = book_service.update_book(book_id, book_data, db)
    return {"book_id": book_id, "book": book}



@router.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_service = BooksService()
    book = book_service.delete_book(book_id, db)
    if book is None:
        return {"message": "Book not found"}
    return {"book_id": book_id, "message": "Book deleted"}  

