from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mesaage" : "hello world"}

@app.get("/name")
def profile():
    return {"name" : "Parth Chauhan"}

