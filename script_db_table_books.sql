CREATE TABLE dev.books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    publication_date DATE NOT NULL,
    price NUMERIC(6, 2) NOT NULL
);