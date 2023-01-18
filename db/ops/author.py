from db.schema import Author
import db.ops.utils


async def create(session, name: str) -> Author:
    rec = Author(name=name)
    session.add(rec)
    await session.commit()
    return rec


async def update(session, author_id: int, name: str) -> Author:
    values = {'name': name}
    return await db.ops.utils.update(session, Author, author_id, values)
