from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Float, String, ForeignKey


Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"{self.id}: name='{self.title}'"


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    author_id = Column(Integer, ForeignKey(Author.id), nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"{self.id}: title='{self.title}' author_id={self.author_id}"