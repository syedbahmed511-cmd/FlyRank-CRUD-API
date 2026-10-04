# FlyRank CRUD API

A CRUD API built with Python, FastAPI, and SQLite for managing tasks.

## Features

- Create tasks
- Read all tasks
- Read a single task
- Update tasks
- Delete tasks
- SQLite database persistence
- Data survives server restarts
- Automatic database and table creation

## Why SQLite?

SQLite was chosen because it is lightweight, requires no separate database server, and stores the database in a single file. This makes it simple and suitable for this project.

## Database

The SQLite database is stored in:

```text
tasks.db
