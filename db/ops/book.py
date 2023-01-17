from db.schema import Book
from db.ops.pagination_window import PaginationWindow, get_pagination_window


async def get(session, limit, offset, order_by, filters) \
        -> PaginationWindow:
    return await get_pagination_window(
        session, 'Book', order_by, limit, offset, filters)


async def create(session, title, author_id) -> Book:
    rec = Book(title=title, author_id=author_id)
    session.add(rec)
    await session.commit()
    return rec
