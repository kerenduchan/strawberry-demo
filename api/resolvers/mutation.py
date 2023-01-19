import strawberry
from api.author import Author
from api.book import Book
from api.count import Count
from db.session import session_maker
import db.schema
import db.utils


async def create_author(name: str) -> Author:
    rec = db.schema.Author(name=name)
    async with session_maker() as session:
        await db.utils.create(session, rec)
        return Author.from_db(rec)


async def update_author(
        author_id: strawberry.ID,
        name: str) -> Author:
    values = {'name': name}

    async with session_maker() as session:
        rec = await db.utils.update(
            session, db.schema.Author, int(author_id), values)
        return Author.from_db(rec)


async def create_book(
        title: str,
        author_id: strawberry.ID) -> Book:
    rec = db.schema.Book(title=title, author_id=author_id)
    async with session_maker() as session:
        await db.utils.create(session, rec)
        return Book.from_db(rec)


async def update_book(
        book_id: strawberry.ID,
        title: str | None = None,
        author_id: int | None = None) -> Book:
    values = {}
    if title is not None:
        values['title'] = title
    if author_id is not None:
        values['author_id'] = author_id

    async with session_maker() as session:
        rec = await db.utils.update(
            session, db.schema.Book, int(book_id), values)
        return Book.from_db(rec)


async def delete_book(book_id: strawberry.ID) -> Count:
    async with session_maker() as session:
        count = await db.utils.delete_book(session, int(book_id))
        return Count(count=count)


async def delete_author(author_id: strawberry.ID) -> Count:
    async with session_maker() as session:
        count = await db.utils.delete_author(session, int(author_id))
        return Count(count=count)
