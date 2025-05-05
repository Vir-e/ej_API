import pytest
from datetime import date
from pydantic import ValidationError
from models.book_DTO import BookDTO


# EL DTO SE CREA CORRECTAMENTE CON LOS TIPOS VÁLIDOS


# TODOS LOS TIPOS SON VÁLIDOS
def test_create_book_dto_valid_types():
    dto = BookDTO(
        title="Rebelión en la granja",
        author="George Orwell",
        publication_date=date(2008, 8, 1),
        price=39.99
    )
    assert dto.title == "Rebelión en la granja"
    assert dto.author == "George Orwell"
    assert dto.publication_date == date(2008, 8, 1)
    assert dto.price == 39.99


# EL TITULO ES UN INT Y DEBE FALLAR
def test_create_book_dto_invalid_title_type():
    with pytest.raises(ValidationError):
        BookDTO(
            title=123,
            author="George Orwell",
            publication_date=date(2008, 8, 1),
            price=39.99
        )


# EL AUTOR ES UN INT Y DEBE FALLAR
def test_create_book_dto_invalid_author_type():
    with pytest.raises(ValidationError):
        BookDTO(
            title="Rebelión en la granja",
            author=456,
            publication_date=date(2008, 8, 1),
            price=39.99
        )


# PUBLICATION_DATE COMO STRING ISO ES CONVERTIDO A DATE
def test_create_book_dto_publication_date_string_accepted():
    dto = BookDTO(
        title="Rebelión en la granja",
        author="George Orwell",
        publication_date="2020-01-01",
        price=19.99
    )
    assert dto.publication_date == date(2020, 1, 1)


# PRICE ES STR Y DEBE FALLAR
def test_create_book_dto_invalid_price_type():
    with pytest.raises(ValidationError):
        BookDTO(
            title="Rebelión en la granja",
            author="George Orwell",
            publication_date=date(2020, 1, 1),
            price="19.99" 
        )