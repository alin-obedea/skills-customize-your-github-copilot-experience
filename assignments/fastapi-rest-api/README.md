# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using FastAPI by creating endpoints, validating request data with Pydantic models, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create Your First FastAPI Endpoint

#### Description
Set up a FastAPI app and create a basic health-check endpoint so you can confirm your API is running.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Add a `GET /health` endpoint that returns `{ "status": "ok" }`
- Run successfully with Uvicorn on `http://127.0.0.1:8000`

### 🛠️ Build CRUD Endpoints for Tasks

#### Description
Create REST endpoints to manage a simple task list in memory.

#### Requirements
Completed program should:

- Define a `Task` model with fields: `id`, `title`, and `completed`
- Add `POST /tasks` to create a task
- Add `GET /tasks` to return all tasks
- Add `PUT /tasks/{task_id}` to update a task's title or completion status
- Add `DELETE /tasks/{task_id}` to remove a task

### 🛠️ Add Validation and Error Handling

#### Description
Improve your API by validating input and returning meaningful error responses.

#### Requirements
Completed program should:

- Use Pydantic validation so `title` is required and at least 3 characters long
- Return `404` when updating or deleting a task that does not exist
- Return clear JSON error messages for invalid operations
- Keep response formats consistent across all endpoints
