from sqlalchemy.ext.asyncio import AsyncSession
import db.utils
import db.schema


async def update_book(
        session: AsyncSession,
        book_id: int,
        title: str | None,
        author_id: int | None) -> db.schema.Book:

    values = {}
    if title is not None:
        values['title'] = title
    if author_id is not None:
        values['author_id'] = author_id

    return await db.utils.update(
        session, db.schema.Book, int(book_id), values)
