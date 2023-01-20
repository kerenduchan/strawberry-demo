from typing import TypeVar, Generic
import strawberry
from api.filters.util import get_operator
import db.filters.number_filter

NumberType = TypeVar("NumberType")


@strawberry.input(description="Filter criteria for number fields.")
class NumberFilter(Generic[NumberType]):
    lt:  NumberType | None = None
    lte: NumberType | None = None
    gt:  NumberType | None = None
    gte: NumberType | None = None
    eq:  NumberType | None = None
    ne:  NumberType | None = None

    def to_db_filter(self, column) -> db.filters.number_filter.NumberFilter:
        op = get_operator(self)

        return db.filters.number_filter.NumberFilter(
            column=column,
            op=op.name,
            value=op.value)
