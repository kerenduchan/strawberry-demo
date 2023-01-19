from dataclasses import dataclass
from typing import Generic, TypeVar, List

T = TypeVar("T")


@dataclass
class PaginationWindow(Generic[T]):
    total_items_count: int
    items: List[T]
