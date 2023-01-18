import dataclasses
from typing import TypeVar, Generic, List, Dict
import sqlalchemy
import db.schema


T = TypeVar("T")


@dataclasses.dataclass
class PaginationWindow(Generic[T]):
    total_items_count: int
    items: List[T]


async def get(
        session,
        class_: T,
        order_by: str,
        limit: int,
        offset: int = 0,
        filters: Dict[str, str] | None = None) -> PaginationWindow:
    """
    Get one pagination window on the given db class for the given limit
    and offset, ordered by the given attribute and filtered using the
    given filters
    """

    order_by_column = getattr(class_, order_by)

    # get the items in the pagination window
    sql = sqlalchemy.select(class_).order_by(order_by_column).limit(limit).offset(offset)
    sql = _append_where_clauses(sql, class_, filters)
    res = await session.execute(sql)
    items = res.scalars().all()

    # get the total items count
    sql = sqlalchemy.select([sqlalchemy.func.count()]).select_from(class_)
    sql = _append_where_clauses(sql, class_, filters)
    res = await session.execute(sql)
    total_items_count = res.scalar()

    return PaginationWindow(
        items=items,
        total_items_count=total_items_count
    )


async def update(session,
                 class_: db.schema.Base,
                 item_id: int,
                 values: Dict):

    # update the db
    sql = sqlalchemy.update(class_).\
        where(class_.id == item_id).\
        values(**values)
    await session.execute(sql)
    await session.commit()

    # return the updated record
    sql = sqlalchemy.select(class_).where(class_.id == item_id)
    res = await session.execute(sql)
    return res.scalars().first()


def _append_where_clauses(sql, class_, filters):
    # This demo only supports filtering by string fields.
    if filters:
        for column_name, val in filters.items():
            column = getattr(class_, column_name)
            sql = sql.where(column.contains(val))
    return sql
