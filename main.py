from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts : list[dict] = [
    {
        "id" : 1,
        "name" : "parth chauhan",
        "title" : "software engineer",
        "age" : 23,
    },
    {
        "id" : 2,
        "name" : "khushal chauhan",
        "title" : "doctor",
        "age" : 24,
    },
]

@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['name']}</h1>"

@app.get("/name")
def profile():
    return {"name" : "Parth Chauhan"}

