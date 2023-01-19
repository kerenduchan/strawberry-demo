from dataclasses import dataclass
import sqlalchemy
from db.filters.i_filter import IFilter


@dataclass
class StringFilter(IFilter):
    column: sqlalchemy.Column
    op: str
    value: str

    def apply(self, sql):
        if self.op == 'contains':
            sql = sql.where(self.column.contains(self.value))
        elif self.op == 'exactly':
            sql = sql.where(self.column == self.value)
        elif self.op == 'starts_with':
            sql = sql.where(self.column.startswith(self.value))
        elif self.op == 'ends_with':
            sql = sql.where(self.column.endswith(self.value))
        return sql
