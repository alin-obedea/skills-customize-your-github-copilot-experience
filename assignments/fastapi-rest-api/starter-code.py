from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3)


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3)
    completed: bool | None = None


class Task(BaseModel):
    id: int
    title: str
    completed: bool


TASKS: list[Task] = []
NEXT_ID = 1


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate) -> Task:
    global NEXT_ID

    task = Task(id=NEXT_ID, title=payload.title, completed=False)
    TASKS.append(task)
    NEXT_ID += 1
    return task


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    return TASKS


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate) -> Task:
    for index, task in enumerate(TASKS):
        if task.id == task_id:
            updated_task = task.model_copy(update=payload.model_dump(exclude_none=True))
            TASKS[index] = updated_task
            return updated_task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict[str, str]:
    for index, task in enumerate(TASKS):
        if task.id == task_id:
            TASKS.pop(index)
            return {"message": "Task deleted"}

    raise HTTPException(status_code=404, detail="Task not found")


# Run with:
# uvicorn starter-code:app --reload
