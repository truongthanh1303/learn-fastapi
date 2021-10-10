from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

class Book(BaseModel):
    title: str
    author: str


@app.get("/")
def index():
    return {
        "data": "Blog list"
    }

@app.get('/blog/{id}')
def show(id: int, limit: int = 10, skip: int = 0, isRequire: Optional[bool] = None):
    return {
        "data": f'{limit} items data from {id} with skip {skip} {isRequire}'
    }

@app.get("/blog/{id}/comments")
def blog_comments(id: int):
    return {
        "blog": {
            'id': id,
            'comments': ['Comment 1', 'Comment 2']
        }
    }

@app.post('/user')
def addUser(user: User = Body(...)):
    return {
        "user": user
    }


@app.post('/rent-book-v1')
def rentBookV1(user: User, book: Book, importance: int = Body(...)):
    # Need the Body syntax in the parametter to force it as the Request Body instead of 
    # the path's query
    
    return {
        "user": user,
        "book": book,
        "importance": importance
    }