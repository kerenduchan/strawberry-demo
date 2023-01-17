from typing import List, Dict, Any
from strawberry.dataloader import DataLoader
import db.schema
from db.session import session_maker
from sqlalchemy import select


def get_all_dataloaders() -> Dict[str, DataLoader]:
    return {
        "author_by_id": DataLoader(load_fn=_get_authors_by_ids),
        "books_by_author_id": DataLoader(load_fn=_get_books_by_author_ids),
    }


async def _get_authors_by_ids(ids: List[str]) -> List[db.schema.Author]:
    return await _get_by_ids('Author', ids)


async def _get_books_by_author_ids(ids: List[int]) -> List[db.schema.Author]:
    return await _get_objects_by_column('Book', 'author_id', ids)


async def _get_by_ids(class_name: str, ids: List[str]) -> List[Any]:
    class_ = getattr(db.schema, class_name)
    async with session_maker() as session:
        sql = select(class_).where(class_.id.in_(ids))
        res = await session.execute(sql)
        recs = res.scalars().all()

    # order the result in the same order as the given ids list
    recs_dict = {r.id: r for r in recs}
    ordered = []
    for id_ in ids:
        ordered.append(recs_dict.get(id_))
    return ordered


async def _get_objects_by_column(
        class_name: str, column_name: str, values: List[Any]) \
        -> List[Any]:
    class_ = getattr(db.schema, class_name)
    column = getattr(class_, column_name)
    async with session_maker() as session:
        sql = select(class_).where(column.in_(values))
        res = await session.execute(sql)
        recs = res.scalars().all()

        # order the results in the same order as the given values list
        groups = {v: [] for v in values}
        for rec in recs:
            groups[getattr(rec, column_name)].append(rec)
        return list(groups.values())
