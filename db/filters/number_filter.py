from dataclasses import dataclass
from typing import TypeVar
import sqlalchemy
from db.filters.i_filter import IFilter


NumberType = TypeVar("NumberType")


@dataclass
class NumberFilter(IFilter):
    column: sqlalchemy.Column
    op: str
    value: NumberType

    def apply(self, stmt):
        db_op = NumberFilter._convert(self.op)
        stmt = stmt.where(eval(f'self.column {db_op} self.value'))
        return stmt

    @staticmethod
    def _convert(op: str) -> str:
        d = {
            'lt': "<",
            'lte': "<=",
            'gt': ">",
            'gte': ">=",
            'eq': "==",
            'ne': "!="
        }
        return d[op]
