from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, String, ForeignKey
import uuid

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"{self.id}: name='{self.title}'"


class Book(Base):
    __tablename__ = "books"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, unique=True, nullable=False)
    author_id = Column(String, ForeignKey(Author.id), nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"{self.id}: title='{self.title}' author_id={self.author_id} price={self.price}"
