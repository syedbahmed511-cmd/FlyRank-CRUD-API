# FlyRank CRUD API

A RESTful Task Management API built using **Python, FastAPI, PostgreSQL, and Docker Compose**.

This project demonstrates CRUD operations, database integration, containerization, and environment-based configuration.

## Tech Stack

- **Python** – Backend programming
- **FastAPI** – REST API framework
- **PostgreSQL 16** – Relational database
- **Docker** – Application containerization
- **Docker Compose** – Multi-container orchestration
- **Uvicorn** – ASGI server

## Project Features

- Create new tasks
- Retrieve all tasks
- Update existing tasks
- Delete tasks
- PostgreSQL database integration
- Persistent database storage
- Dockerized application and database
- Environment variable configuration

## Project Structure

```text
FlyRank-CRUD-API/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── .env.example
├── .gitignore
└── README.md
```

*Additional files may be present depending on the implementation.*

## Prerequisites

Make sure you have installed:

- Python 3.10 or later
- Docker Desktop
- Git

## Environment Configuration

Create a `.env` file in the project root directory.

Example configuration:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=tasks_db
DATABASE_URL=postgresql://postgres:your_password@db:5432/tasks_db
```

A `.env.example` file is also included as a template for environment configuration.

**Important:** Keep your actual `.env` file private and never commit database passwords or credentials to GitHub.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/syedbahmed511-cmd/FlyRank-CRUD-API.git
```

### 2. Navigate to the Project Directory

```bash
cd FlyRank-CRUD-API
```

### 3. Configure Environment Variables

Create your `.env` file using `.env.example` as a reference.

### 4. Build and Start Docker Containers

```bash
docker compose up --build -d
```

This starts two services:

- **App:** FastAPI application
- **DB:** PostgreSQL database

### 5. Verify Running Containers

```bash
docker compose ps
```

### 6. View Application Logs

```bash
docker compose logs --tail=50 app
```

## API Documentation

Once the application is running, access the interactive Swagger documentation:

**http://localhost:8000/docs**

Alternative OpenAPI documentation:

**http://localhost:8000/openapi.json**

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | Retrieve all tasks |
| PUT | `/tasks/{id}` | Update an existing task |
| DELETE | `/tasks/{id}` | Delete a task |

*The endpoints above reflect the current CRUD interface; consult Swagger for exact request and response schemas.*

## Database

The project uses **PostgreSQL 16** as its relational database.

Docker Compose manages the PostgreSQL service alongside the FastAPI application.

Database persistence is provided through the configured database storage volume.

## Useful Docker Commands

Start containers:

```bash
docker compose up -d
```

Rebuild containers:

```bash
docker compose up --build -d
```

View running containers:

```bash
docker compose ps
```

View application logs:

```bash
docker compose logs app
```

View database logs:

```bash
docker compose logs db
```

Stop containers:

```bash
docker compose down
```

Stop containers and remove database volumes (WARNING: deletes persisted database data):

```bash
docker compose down -v
```

## Testing

The API can be tested through FastAPI Swagger UI.

The following CRUD operations have been exercised:

- Task creation
- Task retrieval
- Task updating
- Task deletion

Application restart testing was also performed to check data persistence.

## Author

**Syed Bilal Ahmed**

GitHub: [syedbahmed511-cmd](https://github.com/syedbahmed511-cmd)

Repository: [FlyRank-CRUD-API](https://github.com/syedbahmed511-cmd/FlyRank-CRUD-API)

---

*Developed as part of the FlyRank internship project.*
