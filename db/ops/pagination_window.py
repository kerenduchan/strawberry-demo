from typing import List, TypeVar, Dict
from sqlalchemy import select, func
import db.schema
import dataclasses

ItemType = TypeVar("ItemType")


@dataclasses.dataclass
class PaginationWindow(List[ItemType]):
    total_items_count: int
    items: List[ItemType]


async def get_pagination_window(
        session,
        class_name: str,
        order_by: str,
        limit: int,
        offset: int = 0,
        filters: Dict[str, str] | None = None) -> PaginationWindow:
    """
    Get one pagination window on the given db class for the given limit
    and offset, ordered by the given attribute and filtered using the
    given filters
    """

    class_ = getattr(db.schema, class_name)

    # get the items in the pagination window
    sql = select(class_).order_by(order_by).limit(limit).offset(offset)
    sql = _append_where_clauses(sql, class_, filters)
    res = await session.execute(sql)
    items = res.scalars().all()

    # get the total items count
    sql = select([func.count()]).select_from(class_)
    sql = _append_where_clauses(sql, class_, filters)
    res = await session.execute(sql)
    total_items_count = res.scalar()

    return PaginationWindow(
        items=items,
        total_items_count=total_items_count
    )


def _append_where_clauses(sql, class_, filters):
    # This demo only supports filtering by string fields.
    if filters:
        for column_name, val in filters.items():
            column = getattr(class_, column_name)
            sql = sql.where(column.contains(val))
    return sql
