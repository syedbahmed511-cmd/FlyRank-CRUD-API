from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello, FlyRank!",
        "project": "CRUD API",
        "stage": 1
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }