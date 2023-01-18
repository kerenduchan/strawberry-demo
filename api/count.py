import strawberry


@strawberry.type(description="A count of how many items were affected.")
class Count:

    count: int = strawberry.field(
        description="How many items were affected.")
