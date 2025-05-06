from repository.db_config import Database
from models.book_DAO import Book
from models.book_DTO import BookDTO
from datetime import date
from mappers.book_mapper import BookMapper
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


class BookCRUD:
   
    def create_book(self, book_data: dict, db: Session):

        book = Book(**book_data)
        try:
            db.add(book)
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise RuntimeError("Database error") from e
        except Exception as e:
            db.rollback()
            raise RuntimeError("Database error") from e
        return book
    


    def get_book(self, book_id, db: Session):
        try:
            book = db.query(Book).filter_by(id=book_id).first()
            if book:
                return BookMapper.convert_dao_to_dto(book)
            else:
                return None
        except SQLAlchemyError as e:
            raise RuntimeError("Database error") from e
        except Exception as e:
            raise RuntimeError("Database error") from e

        

    def get_all_books(self, db: Session, limit: int = 10, offset: int = 0):
        try:
            books = db.query(Book).offset(offset).limit(limit).all()
            if books:
                return [BookMapper.convert_dao_to_dto(book) for book in books]
            else:
                return []
        except SQLAlchemyError as e:
            raise RuntimeError("Database error") from e
        except Exception as e:
            raise RuntimeError("Database error") from e



    def update_book(self, book_id, book_data, db: Session):
        try:
            book = db.query(Book).filter_by(id=book_id).first()
            if book:
                for key, value in book_data.items():
                    setattr(book, key, value)
                db.commit()
                return BookMapper.convert_dao_to_dto(book)
            else:
                return None
        except SQLAlchemyError as e:
            db.rollback()
            raise RuntimeError("Database error") from e
        except Exception as e:
            db.rollback()
            raise RuntimeError("Database error") from e



    def delete_book(self, book_id, db: Session):
        try:
            book = db.query(Book).filter_by(id=book_id).first()
            if book:
                db.delete(book)
                db.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            db.rollback()
            raise RuntimeError("Database error") from e
        except Exception as e:
            db.rollback()
            raise RuntimeError("Database error") from e