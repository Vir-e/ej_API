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
    
