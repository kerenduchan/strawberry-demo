from sqlalchemy.ext.asyncio import AsyncSession
from db.schema import Book
import db.ops.utils
from db.ops.pagination_window import PaginationWindow
from db.utils.books_filter import BooksFilter


async def get_books(
        session: AsyncSession,
        order_by: str | None = "name",
        title: str | None = None,
        limit: int = 100,
        offset: int = 0) -> PaginationWindow[Book]:

    db_filter = BooksFilter(title)
    return await db.ops.utils.get(
        session, Book, order_by, db_filter, limit, offset)


async def create_book(
        session: AsyncSession,
        title: str,
        author_id: int) -> Book:
    rec = Book(title=title, author_id=author_id)
    return await db.ops.utils.create(session, rec)


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

    return await db.ops.utils.update(
        session, Book, int(book_id), values)


async def delete_book(
        session: AsyncSession,
        book_id: int) -> int:
    return await db.ops.utils.delete(session, Book, book_id)
