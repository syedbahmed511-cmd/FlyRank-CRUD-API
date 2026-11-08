
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from repository import PostgresRepository

app = FastAPI()

repository = PostgresRepository()


# -------------------------
# Request models
# -------------------------

class TaskCreate(BaseModel):
    title: str | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None


# -------------------------
# Basic endpoints
# -------------------------

@app.get("/")
def home():
    return {
        "message": "Hello, FlyRank!",
        "project": "CRUD API",
        "stage": 3
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


# -------------------------
# GET all tasks
# -------------------------

@app.get("/tasks")
def get_tasks():
    rows = repository.get_all()

    return [
        {
            "id": row["id"],
            "title": row["title"],
            "done": bool(row["done"])
        }
        for row in rows
    ]


# -------------------------
# GET one task
# -------------------------

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    row = repository.get_by_id(task_id)

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "id": row["id"],
        "title": row["title"],
        "done": bool(row["done"])
    }


# -------------------------
# POST create task
# -------------------------

@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    if task_data.title is None or not task_data.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title is required"
        )

    row = repository.create(task_data.title.strip())

    return {
        "id": row["id"],
        "title": row["title"],
        "done": bool(row["done"])
    }


# -------------------------
# PUT update task
# -------------------------

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate):
    row = repository.get_by_id(task_id)

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if task_data.title is not None and not task_data.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    title = (
        task_data.title.strip()
        if task_data.title is not None
        else row["title"]
    )

    done = (
        task_data.done
        if task_data.done is not None
        else bool(row["done"])
    )

    updated_row = repository.update(task_id, title, done)

    return {
        "id": updated_row["id"],
        "title": updated_row["title"],
        "done": bool(updated_row["done"])
    }

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    row = repository.get_by_id(task_id)

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    repository.delete(task_id)

    return
