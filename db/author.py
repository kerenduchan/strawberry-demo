import sqlalchemy
from db.schema import Author, Book
from sqlalchemy.ext.asyncio import AsyncSession


async def delete_author(session: AsyncSession, author_id: int) -> int:
    # check if this author has any books
    sql = sqlalchemy.select(Book).\
        where(Book.author_id == author_id).limit(1)
    res = await session.execute(sql)
    has_books = res.first()

    if has_books:
        raise Exception('cannot delete an author that has books')

    sql = sqlalchemy.delete(Author).\
        where(Author.id == author_id)
    res = await session.execute(sql)
    await session.commit()
    return res.rowcount
