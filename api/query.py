import strawberry
from api.author import Author
from api.book import Book
from api.pagination_window import PaginationWindow
import api.utils.resolvers.query


@strawberry.type
class Query:

    books: PaginationWindow[Book] = strawberry.field(
        resolver=api.utils.resolvers.query.books,
        description="get books")

    authors: PaginationWindow[Author] = strawberry.field(
        resolver=api.utils.resolvers.query.authors,
        description="get authors")

