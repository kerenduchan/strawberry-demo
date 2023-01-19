from db.utils.i_db_filter import IDbFilter
from db.schema import Author, Book
import sqlalchemy


class AuthorsFilter(IDbFilter):
    has_books: bool | None

    def __init__(self, has_books: bool | None):
        self.has_books = has_books

    def apply(self, sql):
        if self.has_books is not None:
            if self.has_books:
                sql = sql.where(Author.id.in_(sqlalchemy.select(Book.author_id).distinct()))
            else:
                sql = sql.where(Author.id.notin_(sqlalchemy.select(Book.author_id).distinct()))
        return sql

