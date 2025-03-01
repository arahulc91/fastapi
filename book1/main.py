from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book(BaseModel):
    id: Optional[int] = Field(default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)


BOOKS = [
    Book(title="The Great Gatsby", author="F. Scott Fitzgerald"),
    Book(title="The Da Vinci Code", author="Dan Brown"),
    Book(title="The Catcher in the Rye", author="J.D. Salinger"),
    Book(title="The Hobbit", author="J.R.R. Tolkien"),
]


@app.get("/books")
async def get_books():
    return BOOKS


@app.get("/books/{title}")
async def get_book_by_title(title: str):
    for book in BOOKS:
        if book.title == title:
            return book
    return None


@app.post("/books")
async def create_book(new_book: Book):
    BOOKS.append(new_book)
    return {"message": "New book added"}


@app.put("/book/{title}")
async def update_book(updated_book: Book):
    for i, book in enumerate(BOOKS):
        if book.title == updated_book.title:
            BOOKS[i] = updated_book
            return {"message": "Book has been updated"}
    return None


@app.delete("/book/{title}")
async def delete_book(title: str):
    for i, book in enumerate(BOOKS):
        if book.title.casefold() == title.casefold():
            BOOKS.pop(i)
            return {"message": "Book has been deleted"}
    return None
