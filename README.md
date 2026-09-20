# FlyRank CRUD API

A simple CRUD API built with Python and FastAPI for managing a to-do task list.

## Features

- Create tasks
- Read all tasks
- Read a single task
- Update tasks
- Delete tasks
- Input validation
- Swagger API documentation

## Installation

Install the required packages:

```bash
python -m pip install "fastapi[standard]"

Run the API
python -m fastapi dev main.py

The API will run at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs

API Endpoints
Method	Endpoint	Description
GET	/	API information
GET	/health	Health check
GET	/tasks	Get all tasks
GET	/tasks/{task_id}	Get one task
POST	/tasks	Create a task
PUT	/tasks/{task_id}	Update a task
DELETE	/tasks/{task_id}	Delete a task
