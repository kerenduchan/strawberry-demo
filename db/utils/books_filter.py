from db.utils.i_db_filter import IDbFilter
from db.schema import Book


class BooksFilter(IDbFilter):
    title: str | None

    def __init__(self, title: bool | None):
        self.title = title

    def apply(self, sql):
        if self.title is not None:
            sql = sql.where(Book.title.contains(self.title))
        return sql
