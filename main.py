from typing import Optional
from fastapi import FastAPI

app = FastAPI()


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
