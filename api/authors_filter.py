import strawberry
import db.utils.authors_filter


@strawberry.input(description="A single author.")
class AuthorsFilter:
    has_books: bool | None = None

    def to_db_filter(self) -> db.utils.authors_filter.AuthorsFilter:
        return db.utils.authors_filter.AuthorsFilter(
            has_books=self.has_books)
