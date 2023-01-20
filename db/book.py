from sqlalchemy.ext.asyncio import AsyncSession
from db.schema import Book
import db.utils


async def create_book(
        session: AsyncSession,
        title: str,
        price: float,
        author_id: str) -> Book:
    rec = Book(title=title, price=price, author_id=author_id)
    return await db.utils.create(session, rec)


async def update_book(
        session: AsyncSession,
        book_id: str,
        title: str | None,
        author_id: str | None) -> Book:
    values = {
        'title': title,
        'author_id': author_id
    }

    return await db.utils.update(
        session, Book, book_id, values)


async def delete_book(
        session: AsyncSession,
        book_id: str) -> int:
    return await db.utils.delete(session, Book, book_id)
