from typing import TYPE_CHECKING, Annotated
import strawberry
import db.schema
import api

if TYPE_CHECKING:
    from api.author import Author


@strawberry.type(description="A single book.")
class Book:

    id: strawberry.ID = strawberry.field(
        description="The ID of this book.")

    title: str = strawberry.field(
        description="The name of this book.")

    author_id: strawberry.ID = strawberry.field(
        description="The ID of the author of this book.")

    @strawberry.field()
    async def author(self, info) -> Annotated["Author", strawberry.lazy("api.author")]:
        rec = await info.context.dataloaders['author_by_id'].load(int(self.author_id))
        return api.author.Author.from_db(rec)

    @classmethod
    def from_db(cls, row: db.schema.Book) -> "Book":
        return cls(id=row.id,
                   title=row.title,
                   author_id=row.author_id)
