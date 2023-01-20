# strawberry-demo

This is a demo project showing how to set up a [Strawberry GraphQL](https://strawberry.rocks/) server (Python).

It features the following:
- An [SQLite](https://www.sqlite.org/index.html) database, accessed through [SQLAlchemy](https://www.sqlalchemy.org/) 
  (async)
- A db schema with two tables: books and authors
- Strawberry fields (author and book) with a [circular dependency](https://strawberry.rocks/docs/types/lazy)
  between them (book has author, author has books)
- GraphQL [queries](https://strawberry.rocks/docs/general/queries) using Strawberry to get books/authors with:
  - [pagination](https://strawberry.rocks/docs/guides/pagination/overview#pagination-at-a-glance)
    ([offset-based](https://strawberry.rocks/docs/guides/pagination/offset-based#implementing-offset-pagination))
  - sorting
  - filtering
- GraphQL [mutations](https://strawberry.rocks/docs/general/mutations) using Strawberry to create/update/delete 
  a book/author
- [Dataloaders](https://strawberry.rocks/docs/guides/dataloaders#dataloaders) for getting the author of a book and 
  getting the books of an author
- FastAPI

# Install
```
python -m venv virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt
```

# Initialize the database
```
python init_db.py
```

# Start the Server
```
uvicorn app:app --reload
```
Then browse to http://127.0.0.1:8000/graphql

# Sample Queries

Get all books (limited to the first 100):
```graphql
query books {
  books {
    items {
      id
      title
      price
      authorId
      author {
        name
        id
      }
    }
    totalItemsCount
  }
}
```

Get the first 3 books whose price is greater than 4.3:
```graphql
query books {
  books(filter: {price: {gt: 4.3}}, limit: 3, orderBy: "price") {
    items {
      id
      title
      price
      authorId
      author {
        name
        id
      }
    }
    totalItemsCount
  }
}
```

Get all authors (limited to the first 100) whose name starts with "Jo":
```graphql
query authors {
  authors(filter: {name: {startsWith: "Jo"}}) {
    items {
      id
      name
      books {
        id
        title
      }
    }
    totalItemsCount
  }
}
```

# Sample Mutations

Create an author named "John Doe":
```graphql
mutation createAuthor {
  createAuthor(name: "John Doe") {
    id
  }
}
```

Create a book for the author whose id is `"8c5db983-b824-4120-b07b-179f97575b77"`
(replace this with a real author ID from your database), with a price of 7.95:
```graphql
mutation createBook {
  createBook(
    title: "Book Title"
    authorId: "8c5db983-b824-4120-b07b-179f97575b77"
    price: 7.95
  ) {
    id
  }
}
```
