from fastapi import Body ,FastAPI

app = FastAPI()

BOOKS = [
    {'title':'one','author':'ram','category':'home','subject':'science'},
    {'title':'two','author':'shyam','category':'work','subject':'hindi'},
    {'title':'three','author':'sita','category':'home','subject':'english'},
    {'title':'gour','author':'laksman','category':'work','subject':'hindi'}
]
@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_all_books(book_title : str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        
@app.get("/books/")   
async def read_subject_query(subject: str):
    book_return = []
    for book in BOOKS:
        if book.get('subject').casefold() == subject.casefold():
            book_return.append(book)
    return book_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
