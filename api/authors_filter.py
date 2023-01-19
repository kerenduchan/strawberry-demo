import strawberry
from api.filters.string_filter import StringFilter
import db.authors_filter
import db.schema


@strawberry.input(description="Filter criteria for authors.")
class AuthorsFilter:
    has_books: bool | None = None
    name: StringFilter | None = None

    def to_db_filter(self) -> db.authors_filter.AuthorsFilter:
        return db.authors_filter.AuthorsFilter(
            has_books=self.has_books,
            name=self.name.to_db_filter(db.schema.Author.name) if self.name else None)
