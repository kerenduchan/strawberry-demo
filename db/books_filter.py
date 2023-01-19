from dataclasses import dataclass
from db.i_db_filter import IDbFilter
from db.filters.number_filter import NumberFilter
from db.filters.string_filter import StringFilter


@dataclass
class BooksFilter(IDbFilter):
    title: StringFilter | None
    price: NumberFilter | None

    def apply(self, sql):
        if self.title is not None:
            sql = self.title.apply(sql)
        if self.price is not None:
            sql = self.price.apply(sql)
        return sql
