import strawberry
from api.author import Author
from api.book import Book
from api.pagination_window import PaginationWindow
import api.query_resolvers


@strawberry.type
class Query:

    books: PaginationWindow[Book] = strawberry.field(
        resolver=api.query_resolvers.books,
        description="get books")

    authors: PaginationWindow[Author] = strawberry.field(
        resolver=api.query_resolvers.authors,
        description="get authors")

