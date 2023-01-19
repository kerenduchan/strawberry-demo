from db.session import session_maker
from api.pagination_window import PaginationWindow
from api.book import Book
from api.author import Author
from api.authors_filter import AuthorsFilter
import db.schema
import db.ops.utils


async def books(
        order_by: str | None = "title",
        limit: int = 100,
        offset: int = 0,
        title: str | None = None) -> PaginationWindow[Book]:

    async with session_maker() as session:
        window = await db.ops.book.get_books(
            session, order_by, title, limit, offset)

        return PaginationWindow[Book](
            items=[Book.from_db(item) for item in window.items],
            total_items_count=window.total_items_count)


async def authors(
        order_by: str | None = "name",
        where: AuthorsFilter | None = None,
        limit: int = 100,
        offset: int = 0) -> PaginationWindow[Author]:

    db_filter = None if where is None else where.to_db_filter()

    async with session_maker() as session:
        window = await db.ops.author.get_authors(
            session, order_by, db_filter, limit, offset)

        return PaginationWindow[Author](
            items=[Author.from_db(item) for item in window.items],
            total_items_count=window.total_items_count)
