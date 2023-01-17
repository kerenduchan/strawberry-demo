from db.schema import Author
from db.ops.pagination_window import PaginationWindow, get_pagination_window


async def get(session, limit, offset, order_by, filters) \
        -> PaginationWindow:
    return await get_pagination_window(
        session, 'Author', order_by, limit, offset, filters)


async def create(session, name) -> Author:
    rec = Author(name=name)
    session.add(rec)
    await session.commit()
    return rec
