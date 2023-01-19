import strawberry
from api.book import Book
from api.author import Author
from api.count import Count
import api.resolvers.mutation


@strawberry.type
class Mutation:

    create_author: Author = strawberry.mutation(
        resolver=api.resolvers.mutation.create_author,
        description="create an author")

    update_author: Author = strawberry.mutation(
        resolver=api.resolvers.mutation.update_author,
        description="update an author")

    delete_author: Count = strawberry.mutation(
        resolver=api.resolvers.mutation.delete_author,
        description="delete an author")

    create_book: Book = strawberry.mutation(
        resolver=api.resolvers.mutation.create_book,
        description="create a book")

    update_book: Book = strawberry.mutation(
        resolver=api.resolvers.mutation.update_book,
        description="update a book")

    delete_book: Count = strawberry.mutation(
        resolver=api.resolvers.mutation.delete_book,
        description="delete a book")
