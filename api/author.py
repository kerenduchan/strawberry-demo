from typing import TYPE_CHECKING, Annotated, List
import strawberry
import db.schema
from api.book import Book


if TYPE_CHECKING:
    from api.book import Book


@strawberry.type(description="A single author.")
class Author:

    id: strawberry.ID = strawberry.field(
        description="The ID of this author.")

    name: str = strawberry.field(
        description="The name of this author.")

    @strawberry.field()
    async def books(self, info) \
            -> List[Annotated["Book", strawberry.lazy("api.book")]]:
        recs = await info.context.dataloaders['books_by_author_id'].load(int(self.id))
        return [Book.from_db(rec) for rec in recs]

    @classmethod
    def from_db(cls, row: db.schema.Author) -> "Author":
        return cls(id=row.id,
                   name=row.name)
