from typing import TypeVar
from api.pagination_window import PaginationWindow
from db.session import session_maker
import db.utils

DEFAULT_LIMIT = 100
ApiClass = TypeVar("ApiClass")


def get_resolver_fn(
        api_class: ApiClass,
        filter_class: type,
        db_class: type,
        default_order_by: str):

    async def resolve(
            order_by: str | None = default_order_by,
            filter: filter_class | None = None,
            limit: int = DEFAULT_LIMIT,
            offset: int = 0) -> PaginationWindow[api_class]:

        db_filter = None if filter is None else filter.to_db_filter()

        async with session_maker() as session:
            window = await db.utils.get(
                session, db_class, order_by, db_filter, limit, offset)

            return PaginationWindow[api_class](
                items=[api_class.from_db(item) for item in window.items],
                total_items_count=window.total_items_count)

    return resolve
