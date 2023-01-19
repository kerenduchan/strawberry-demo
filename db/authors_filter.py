import sqlalchemy
from db.i_db_filter import IDbFilter
from db.schema import Author, Book
from db.filters.string_filter import StringFilter


class AuthorsFilter(IDbFilter):
    has_books: bool | None
    name: StringFilter | None

    def __init__(self, has_books: bool | None, name: StringFilter | None):
        self.has_books = has_books
        self.name = name

    def apply(self, sql):
        if self.has_books is not None:
            if self.has_books:
                sql = sql.where(Author.id.in_(sqlalchemy.select(Book.author_id).distinct()))
            else:
                sql = sql.where(Author.id.notin_(sqlalchemy.select(Book.author_id).distinct()))

        if self.name is not None:
            sql = self.name.apply(sql)

        return sql
