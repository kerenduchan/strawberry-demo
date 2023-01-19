from sqlalchemy.ext.asyncio import AsyncSession
from db.schema import Book
import db.utils


async def create_book(
        session: AsyncSession,
        title: str,
        price: float,
        author_id: int) -> Book:
    rec = Book(title=title, price=price, author_id=author_id)
    return await db.utils.create(session, rec)


async def update_book(
        session: AsyncSession,
        book_id: int,
        title: str | None,
        author_id: int | None) -> Book:
    values = {}
    if title is not None:
        values['title'] = title
    if author_id is not None:
        values['author_id'] = author_id

    return await db.utils.update(
        session, Book, int(book_id), values)


async def delete_book(
        session: AsyncSession,
        book_id: int) -> int:
    return await db.utils.delete(session, Book, book_id)
