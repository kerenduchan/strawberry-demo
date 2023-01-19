import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession
from db.schema import Author, Book
from db.pagination_window import PaginationWindow
import db.utils
from db.authors_filter import AuthorsFilter


async def get_authors(
        session: AsyncSession,
        order_by: str | None = "name",
        db_filter: AuthorsFilter | None = None,
        limit: int = 100,
        offset: int = 0) -> PaginationWindow[Author]:

    return await db.utils.get(
        session, Author, order_by, db_filter, limit, offset)


async def create_author(
        session: AsyncSession,
        name: str) -> Author:
    rec = db.schema.Author(name=name)
    return await db.utils.create(session, rec)


async def update_author(
        session: AsyncSession,
        author_id: int,
        name: str) -> Author:
    values = {'name': name}
    return await db.utils.update(
        session, db.schema.Author, int(author_id), values)


async def delete_author(
        session: AsyncSession,
        author_id: int) -> int:
    # check if this author has any books
    sql = sqlalchemy.select(Book).\
        where(Book.author_id == author_id).limit(1)
    res = await session.execute(sql)
    has_books = res.first()

    if has_books:
        raise Exception('cannot delete an author that has books')

    return await db.utils.delete(session, Author, author_id)
