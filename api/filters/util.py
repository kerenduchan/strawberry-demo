from typing import TypeVar
from dataclasses import dataclass

T = TypeVar("T")


@dataclass
class Operator:
    name: str
    value: T


def get_operator(obj) -> Operator:
    all_ops = obj.__dict__.items()
    set_ops = [(op, val) for op, val in all_ops if val is not None]

    if len(set_ops) != 1:
        raise Exception('exactly one operator must be specified')

    set_op = set_ops[0]
    return Operator(name=set_op[0], value=set_op[1])