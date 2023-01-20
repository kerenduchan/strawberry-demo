import strawberry
from api.filters.util import get_operator
import db.filters.string_filter


@strawberry.input(description="Filter criteria for string fields.")
class StringFilter:
    contains:  str | None = None
    exactly:  str | None = None
    starts_with:  str | None = None
    ends_with:  str | None = None

    def to_db_filter(self, column) -> db.filters.string_filter.StringFilter:
        op = get_operator(self)

        return db.filters.string_filter.StringFilter(
            column=column,
            op=op.name,
            value=op.value)
