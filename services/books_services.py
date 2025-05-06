from repository.books_crud import BookCRUD
from models.book_DTO import BookDTO
from sqlalchemy.orm import Session



class BooksService:


    def create_book(self, book_dto: BookDTO, db: Session):
        book_crud = BookCRUD()
        try:
            book_create = book_crud.create_book(book_dto.__dict__, db)
        except RuntimeError as e:
            raise RuntimeError("Database error") from e
        except Exception as e:
            raise RuntimeError("Database error") from e
        return book_create


    def get_books(self, db: Session, limit: int = 10, offset: int = 0):
        book_crud = BookCRUD()
        try:
            books = book_crud.get_all_books(db, limit, offset)
        except RuntimeError as e:
            raise RuntimeError("Database error") from e
        except Exception as e:
            raise RuntimeError("Database error") from e
        return books
    

    def get_book(self, book_id: int, db: Session):
        book_crud = BookCRUD()
        try:
            book = book_crud.get_book(book_id, db)
        except RuntimeError as e:
            raise RuntimeError("Database error") from e
        except Exception as e:
            raise RuntimeError("Database error") from e
        return book
    

    def update_book(self, book_id: int, book_dto: BookDTO, db: Session):
        book_crud = BookCRUD()
        try:
            book = book_crud.update_book(book_id, book_dto.__dict__, db)
        except RuntimeError as e:
            raise RuntimeError("Database error") from e
        except Exception as e:
            raise RuntimeError("Database error") from e
        return book
    

    def delete_book(self, book_id: int, db: Session):
        book_crud = BookCRUD()
        try:
            book_deleted = book_crud.delete_book(book_id, db)
        except RuntimeError as e:
            raise RuntimeError("Database error") from e
        except Exception as e:
            raise RuntimeError("Database error") from e
        return book_deleted


