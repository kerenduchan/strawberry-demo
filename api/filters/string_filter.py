import strawberry
import db.filters.string_filter


@strawberry.input(description="Filter criteria for string fields.")
class StringFilter:
    contains:  str | None = None
    exactly:  str | None = None
    starts_with:  str | None = None
    ends_with:  str | None = None

    def to_db_filter(self, column) -> db.filters.string_filter.StringFilter:

        all_ops = {
            'contains': self.contains,
            'exactly': self.exactly,
            'starts_with': self.starts_with,
            'ends_with': self.ends_with,
        }
        ops = [(op, val) for op, val in all_ops.items() if val is not None]

        if len(ops) != 1:
            raise Exception('exactly one operator must be specified')

        (op, value) = ops[0]

        return db.filters.string_filter.StringFilter(
            column=column,
            op=op,
            value=value)
