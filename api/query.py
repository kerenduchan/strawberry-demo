import strawberry
from api.author import Author
from api.book import Book
from api.pagination_window import PaginationWindow
from db.session import session_maker
import db.schema
import db.ops


@strawberry.type
class Query:

    @strawberry.field
    async def books(self,
                    order_by: str | None = "title",
                    limit: int = 100,
                    offset: int = 0,
                    title: str | None = None) -> PaginationWindow[Book]:
        filters = {}
        if title:
            filters['title'] = title

        async with session_maker() as session:
            window = await db.ops.utils.get(
                session, db.schema.Book, order_by, limit, offset, filters)

            return PaginationWindow[Book](
                items=[Book.from_db(item) for item in window.items],
                total_items_count=window.total_items_count)

    @strawberry.field
    async def authors(self,
                      order_by: str | None = "name",
                      limit: int = 100,
                      offset: int = 0,
                      name: str | None = None) -> PaginationWindow[Author]:
        filters = {}
        if name:
            filters['name'] = name

        async with session_maker() as session:
            window = await db.ops.utils.get(
                session, db.schema.Author, order_by, limit, offset, filters)

            return PaginationWindow[Author](
                items=[Author.from_db(item) for item in window.items],
                total_items_count=window.total_items_count)
