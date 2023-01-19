import strawberry
import db.authors_filter


@strawberry.input(description="A single author.")
class AuthorsFilter:
    has_books: bool | None = None
    name: str | None = None

    def to_db_filter(self) -> db.authors_filter.AuthorsFilter:
        return db.authors_filter.AuthorsFilter(
            has_books=self.has_books,
            name=self.name)
