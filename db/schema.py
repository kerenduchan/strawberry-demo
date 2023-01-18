from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    author_id = Column(Integer, ForeignKey(Author.id), nullable=False)
