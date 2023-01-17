from sqlalchemy import select
from db.schema import Book


async def get(session, order_by):
    sql = select(Book).order_by(order_by)
    res = await session.execute(sql)
    return res.scalars().all()


async def create(session, title, author_id) -> Book:
    rec = Book(title=title, author_id=author_id)
    session.add(rec)
    await session.commit()
    return rec
