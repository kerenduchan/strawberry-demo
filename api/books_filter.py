import strawberry
import db.books_filter


@strawberry.input(description="Filter criteria for books.")
class BooksFilter:
    title: str | None = None

    def to_db_filter(self) -> db.books_filter.BooksFilter:
        return db.books_filter.BooksFilter(
            title=self.title)
