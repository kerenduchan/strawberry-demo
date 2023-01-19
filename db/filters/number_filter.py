from dataclasses import dataclass
from db.filters.i_filter import IFilter


@dataclass
class NumberFilter(IFilter):
    column: type
    op: str
    value: float

    def apply(self, stmt):
        stmt = stmt.where(eval(f'self.column {self.op} self.value'))
        return stmt
