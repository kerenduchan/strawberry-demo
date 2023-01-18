import strawberry
from api.book import Book
from api.author import Author
from db.session import session_maker
import db.schema
from db.utils import create, update

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def create_author(self, name: str) -> Author:
        rec = db.schema.Author(name=name)
        async with session_maker() as session:
            await create(session, rec)
            return Author.from_db(rec)

    @strawberry.mutation
    async def update_author(self,
                            author_id: strawberry.ID,
                            name: str) -> Author:
        values = {'name': name}

        async with session_maker() as session:
            rec = await update(
                session, db.schema.Author, int(author_id), values)
            return Author.from_db(rec)

    @strawberry.mutation
    async def create_book(self,
                          title: str,
                          author_id: strawberry.ID) -> Book:
        rec = db.schema.Book(title=title, author_id=author_id)
        async with session_maker() as session:
            await create(session, rec)
            return Book.from_db(rec)

    @strawberry.mutation
    async def update_book(self,
                          book_id: strawberry.ID,
                          title: str | None = None,
                          author_id: int | None = None) -> Book:
        values = {}
        if title is not None:
            values['title'] = title
        if author_id is not None:
            values['author_id'] = author_id

        async with session_maker() as session:
            rec = await update(
                session, db.schema.Book, int(book_id), values)
            return Book.from_db(rec)
