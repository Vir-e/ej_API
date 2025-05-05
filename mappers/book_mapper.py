from models.book_DTO import BookDTO
from models.book_DAO import Book

class BookMapper:
    
    @staticmethod
    def convert_dao_to_dto(book_dao: Book) -> BookDTO:
        return BookDTO(
            title=book_dao.title,
            author=book_dao.author,
            publication_date=book_dao.publication_date,
            price=book_dao.price
        )
    
    @staticmethod
    def convert_dto_to_dao(book_dto: BookDTO) -> Book:
        return Book(
            title=book_dto.title,
            author=book_dto.author,
            publication_date=book_dto.publication_date,
            price=book_dto.price
        )