from dataclasses import dataclass
from db.i_db_filter import IDbFilter
from db.filters.number_filter import NumberFilter
from db.schema import Book


@dataclass
class BooksFilter(IDbFilter):
    title: str | None
    price: NumberFilter | None

    def apply(self, sql):
        if self.title is not None:
            sql = sql.where(Book.title.contains(self.title))
        if self.price is not None:
            sql = self.price.apply(sql)
        return sql
