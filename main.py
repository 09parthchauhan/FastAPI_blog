from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mesaage" : "hello world"}



