from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

DATABASE = "tasks.db"


# -------------------------
# Database connection
# -------------------------

def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


# -------------------------
# Initialize database
# -------------------------

def initialize_database():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT 0
        )
    """)

    count = connection.execute(
        "SELECT COUNT(*) FROM tasks"
    ).fetchone()[0]

    if count == 0:
        connection.executemany(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            [
                ("Learn FastAPI", 0),
                ("Build CRUD API", 0),
                ("Upload project to GitHub", 1)
            ]
        )

    connection.commit()
    connection.close()


initialize_database()


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
        "stage": 2
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
    connection = get_db_connection()

    rows = connection.execute(
        "SELECT id, title, done FROM tasks"
    ).fetchall()

    connection.close()

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
    connection = get_db_connection()

    row = connection.execute(
        "SELECT id, title, done FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    connection.close()

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

    # Validate title
    if task_data.title is None or not task_data.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title is required"
        )

    connection = get_db_connection()

    # Insert task into SQLite
    cursor = connection.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (task_data.title.strip(), 0)
    )

    connection.commit()

    # Get ID of newly created task
    new_task_id = cursor.lastrowid

    # Get the newly created task
    row = connection.execute(
        "SELECT id, title, done FROM tasks WHERE id = ?",
        (new_task_id,)
    ).fetchone()

    connection.close()

    return {
        "id": row["id"],
        "title": row["title"],
        "done": bool(row["done"])
    }