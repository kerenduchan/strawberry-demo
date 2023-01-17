from typing import List
from sqlalchemy import select
from db.schema import Author


async def get(session, order_by: str) -> List[Author]:
    sql = select(Author).order_by(order_by)
    res = await session.execute(sql)
    return res.scalars().all()


async def create(session, name) -> Author:
    rec = Author(name=name)
    session.add(rec)
    await session.commit()
    return rec
