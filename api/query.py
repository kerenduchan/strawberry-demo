from typing import Dict, TypeVar
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

        resolve = _get_resolver(db.schema.Book, Book)
        return await resolve(order_by, limit, offset, filters)

    @strawberry.field
    async def authors(self,
                      order_by: str | None = "name",
                      limit: int = 100,
                      offset: int = 0,
                      name: str | None = None) -> PaginationWindow[Author]:
        filters = {}

        if name:
            filters['name'] = name

        resolve = _get_resolver(db.schema.Author, Author)
        return await resolve(order_by, limit, offset, filters)


DbClass = TypeVar("DbClass")
ApiClass = TypeVar("ApiClass")


def _get_resolver(db_class: DbClass, api_class: ApiClass | Author):

    async def resolve(order_by: str,
                      limit: int = 100,
                      offset: int = 0,
                      filters: Dict[str, str] | None = None) \
            -> PaginationWindow[api_class]:

        async with session_maker() as session:
            window = await db.ops.utils.get(
                session, db_class, order_by, limit, offset, filters)

            return PaginationWindow[api_class](
                items=[api_class.from_db(item) for item in window.items],
                total_items_count=window.total_items_count)

    return resolve
