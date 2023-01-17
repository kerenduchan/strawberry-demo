import strawberry
from typing import List, TypeVar


GenericType = TypeVar("GenericType")


@strawberry.type
class PaginationWindow(List[GenericType]):
    items: List[GenericType] = strawberry.field(
        description="The list of items in this pagination window."
    )

    total_items_count: int = strawberry.field(
        description="Total number of items in the filtered dataset."
    )
