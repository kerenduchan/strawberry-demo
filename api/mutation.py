import strawberry
from api.book import Book
from api.author import Author
from db.session import session_maker
import db.ops.book
import db.ops.author


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def create_author(self, name: str) -> Author:
        async with session_maker() as session:
            rec = await db.ops.author.create(
                session=session,
                name=name)
        return Author.from_db(rec)

    @strawberry.mutation
    async def update_author(self, name: str) -> Author:
        async with session_maker() as session:
            rec = await db.ops.author.create(
                session=session,
                name=name)
        return Author.from_db(rec)

    @strawberry.mutation
    async def create_book(self, title: str, author_id: strawberry.ID) -> Book:
        async with session_maker() as session:
            rec = await db.ops.book.create(
                session=session,
                title=title,
                author_id=author_id)
        return Book.from_db(rec)

