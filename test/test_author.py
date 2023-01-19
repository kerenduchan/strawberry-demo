import asyncio
import db.session
import db.ops.author


async def main():
    async with db.session.session_maker() as session:
        res = await db.ops.author.get_authors(session, "name", True)
        print(res)

asyncio.run(main())
