from typing import List
import strawberry
from api.book import Book
from api.author import Author
from db.session import session_maker
import db.ops.book


@strawberry.type
class Query:

    @strawberry.field
    async def books(self, order_by: str | None = "title") -> List[Book]:
        async with session_maker() as session:
            return await db.ops.book.get(session, order_by)

    @strawberry.field
    async def authors(self, order_by: str | None = "name") -> List[Author]:
        async with session_maker() as session:
            return await db.ops.author.get(session, order_by)
