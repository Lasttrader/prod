from fastapi import FastAPI

app = FastAPI()

@app.get("/fastapi")
def main():
    return {"hello" : "fastapi"}
