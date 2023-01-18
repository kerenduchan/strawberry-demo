from db.schema import Book
import db.ops.utils


async def create(session, title: str, author_id: int) -> Book:
    rec = Book(title=title, author_id=author_id)
    session.add(rec)
    await session.commit()
    return rec


async def update(session, book_id: int, title: str) -> Book:
    values = {'title': title}
    return await db.ops.utils.update(session, "Book", book_id, values)
