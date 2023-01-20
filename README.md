# strawberry-demo

This is a demo project showing how to set up a **[Strawberry](https://strawberry.rocks/) GraphQL** server (Python).
It features the following:
- sqlite database, accessed through **[SQLAlchemy](https://www.sqlalchemy.org/) async**.
- A db schema with two tables: books and authors
- Strawberry fields (author and book) with a **cyclic dependency** between them (book has author, author has books)
- **GraphQL queries** using Strawberry to get books/authors with **pagination** (offset-based), **sorting**, and **filtering**.
- **GraphQL mutations** using Strawberry to create/update/delete a book/author.
- **Dataloaders** for getting the author of a book and getting the books of an author.
- **FastAPI**

# Installation
```
python -m venv virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt
```

# Starting the Server
```
uvicorn app:app --reload
```
Then browse to http://127.0.0.1:8000/graphql.

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
  books(filter: { price: { gte: 4.44}}, limit: 3, orderBy: "price") {
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
authors(filter: { name: { startsWith: "Jo" }}) {
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

Create a book for the author whose id is 1, with a price of 7.95:
```graphql
mutation createBook {
  createBook(title: "Book Title", authorId: 1, price: 7.95) {
    id
  }
}
```
