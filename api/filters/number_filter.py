import strawberry
import db.filters.number_filter


@strawberry.input(description="Filter criteria for number fields.")
class NumberFilter:
    lt:  float | None = None
    lte: float | None = None
    gt:  float | None = None
    gte: float | None = None
    eq:  float | None = None
    ne:  float | None = None

    def to_db_filter(self, column) -> db.filters.number_filter.NumberFilter:

        all_ops = {
            '<': self.lt,
            '<=': self.lte,
            '>': self.gt,
            '>=': self.gte,
            '==': self.eq,
            '!=': self.ne}

        ops = [(op, val) for op, val in all_ops.items() if val is not None]

        if len(ops) != 1:
            raise Exception('exactly one operator must be specified')

        (op, value) = ops[0]

        return db.filters.number_filter.NumberFilter(
            column=column,
            op=op,
            value=value)
