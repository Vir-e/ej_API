from repository.books_crud import BookCRUD
from repository.db_config import Database
from models.book_DTO import BookDTO
#from models.book_DAO import Book
from datetime import date
from sqlalchemy.orm import Session



class BooksService:


    def create_book(self, book_dto: BookDTO, db: Session):
        book_crud = BookCRUD()
        book_create = book_crud.create_book(book_dto.__dict__, db)
        return book_create


    def get_books(self, db: Session):
        book_crud = BookCRUD()
        books = book_crud.get_all_books(db)
        return books
    

    def get_book(self, book_id: int, db: Session):
        book_crud = BookCRUD()
        book = book_crud.get_book(book_id, db)
        if book is None:
            return {"message": "Book not found"}
        return book
    

    def update_book(self, book_id: int, book_dto: BookDTO, db: Session):
        book_crud = BookCRUD()
        book = book_crud.update_book(book_id, book_dto.__dict__, db)
        if book is None:
            return {"message": "Book not found"}
        return book
    

    def delete_book(self, book_id: int, db: Session):
        book_crud = BookCRUD()
        book = book_crud.delete_book(book_id, db)
        if book is None:
            return {"message": "Book not found"}
        return book


