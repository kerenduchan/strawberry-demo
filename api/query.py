import strawberry
from api.pagination_window import PaginationWindow
from api.query_resolvers import get_resolver_fn

from api.author import Author
from api.authors_filter import AuthorsFilter
import db.author

from api.book import Book
from api.books_filter import BooksFilter
import db.book


@strawberry.type
class Query:

    books: PaginationWindow[Book] = strawberry.field(
        resolver=get_resolver_fn(Book, BooksFilter, db.book.Book, "title"),
        description="get books")

    authors: PaginationWindow[Author] = strawberry.field(
        resolver=get_resolver_fn(Author, AuthorsFilter, db.author.Author, "name"),
        description="get authors")
