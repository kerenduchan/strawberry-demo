import strawberry
from api.filters.number_filter import NumberFilter
import db.books_filter
import db.schema


@strawberry.input(description="Filter criteria for books.")
class BooksFilter:
    title: str | None = None
    price: NumberFilter | None = None

    def to_db_filter(self) -> db.books_filter.BooksFilter:
        return db.books_filter.BooksFilter(
            title=self.title,
            price=self.price.to_db_filter(db.schema.Book.price) if self.price else None)
