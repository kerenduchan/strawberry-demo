from db.session import session_maker
from api.pagination_window import PaginationWindow
from api.book import Book
from api.author import Author
from api.authors_filter import AuthorsFilter
from api.books_filter import BooksFilter
import db.schema
import db.utils
import db.book
import db.author

DEFAULT_LIMIT = 100

async def books(
        order_by: str | None = "title",
        filter: BooksFilter | None = None,
        limit: int = DEFAULT_LIMIT,
        offset: int = 0,
        title: str | None = None) -> PaginationWindow[Book]:

    db_filter = None if filter is None else filter.to_db_filter()

    async with session_maker() as session:
        window = await db.book.get_books(
            session, order_by, db_filter, limit, offset)

        return PaginationWindow[Book](
            items=[Book.from_db(item) for item in window.items],
            total_items_count=window.total_items_count)


async def authors(
        order_by: str | None = "name",
        filter: AuthorsFilter | None = None,
        limit: int = DEFAULT_LIMIT,
        offset: int = 0) -> PaginationWindow[Author]:

    db_filter = None if filter is None else filter.to_db_filter()

    async with session_maker() as session:
        window = await db.author.get_authors(
            session, order_by, db_filter, limit, offset)

        return PaginationWindow[Author](
            items=[Author.from_db(item) for item in window.items],
            total_items_count=window.total_items_count)
