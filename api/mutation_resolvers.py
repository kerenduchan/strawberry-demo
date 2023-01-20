import strawberry
from api.author import Author
from api.book import Book
from api.count import Count
from db.session import session_maker
import db.author
import db.book


async def create_author(name: str) -> Author:
    async with session_maker() as session:
        rec = await db.author.create_author(session, name)
        return Author.from_db(rec)


async def update_author(
        author_id: strawberry.ID,
        name: str) -> Author:

    async with session_maker() as session:
        rec = await db.author.update_author(session, author_id, name)
        return Author.from_db(rec)


async def delete_author(author_id: strawberry.ID) -> Count:
    async with session_maker() as session:
        count = await db.author.delete_author(session, author_id)
        return Count(count=count)


async def create_book(
        title: str,
        price: float,
        author_id: strawberry.ID) -> Book:
    async with session_maker() as session:
        rec = await db.book.create_book(session, title, price, author_id)
        return Book.from_db(rec)


async def update_book(
        book_id: strawberry.ID,
        title: str | None = None,
        author_id: str | None = None) -> Book:

    async with session_maker() as session:
        rec = await db.book.update_book(session, book_id, title, author_id)
        return Book.from_db(rec)


async def delete_book(book_id: strawberry.ID) -> Count:
    async with session_maker() as session:
        count = await db.book.delete_book(session, book_id)
        return Count(count=count)
