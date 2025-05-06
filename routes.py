from fastapi import APIRouter, Depends, HTTPException, Query
from models.book_DTO import BookDTO
from sqlalchemy.orm import Session
from dependencies.dependencies import get_db
from services.books_services import BooksService
from typing import List

router = APIRouter()



@router.get("/books/", response_model=List[BookDTO])
def get_books(db: Session = Depends(get_db),
            offset: int = Query(0),
            limit: int = Query(10)):
    book_service = BooksService()
    books = book_service.get_books(db, limit=limit, offset=offset)
    return books



@router.get("/books/{book_id}", response_model=BookDTO)
def get_book(book_id: int, Session = Depends(get_db)):
    try:
        book_service = BooksService()
        book = book_service.get_book(book_id, Session)
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return book
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail="Database error")



@router.post("/books/")
def create_book(book_data: BookDTO, db: Session = Depends(get_db)):
    book_service = BooksService()
    book_create = book_service.create_book(book_data, db)
    if book_create is None:
        raise HTTPException(status_code=400, detail="Book creation failed")
    return book_data



@router.put("/books/{book_id}")
def update_book(book_id: int, book_data: BookDTO, db: Session = Depends(get_db)):
    book_service = BooksService()
    book = book_service.update_book(book_id, book_data, db)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_data



@router.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_service = BooksService()
    book_deleted = book_service.delete_book(book_id, db)
    if book_deleted is False:
        raise HTTPException(status_code=404, detail="Book deleted failed")
    return True 

