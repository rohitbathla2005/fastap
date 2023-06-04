from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

class Book:
    id: int
    title: str
    author:str
    description:str
    rating:int

    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
class BookRequest(BaseModel):
    id: int
    title: str= Field(min_length=3)
    author:str
    description:str=Field(min_length=3,max_length=999)
    rating:int=Field(gt=0,lt=6)

BOOKS = [
    Book(1, 'ram1', 'rama1', 'nice1', 5),
    Book(2, 'ram1', 'rama1', 'nice1', 5),
    Book(3, 'ram1', 'rama1', 'nice1', 5),
    Book(4, 'ram1', 'rama1', 'nice1', 5),
]

@app.get("/books")
async def read__all():
    return BOOKS

@app.post("/create_book")
async def create_book(book_request : BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_id(new_book))

@app.get("/books/{book_id}")
async def read__all(book_id:int):
    for book in BOOKS:
        if book.id==book_id:
            return book

@app.put("/books/update_book")
async def update_book(book_request : BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_request.id:
                BOOKS[i] = book_request

def find_id(book:Book):
    if len(BOOKS) >0:
        book.id = BOOKS[-1].id+1
    else:
        book.id = -1
    return book