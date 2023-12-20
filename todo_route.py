from fastapi import APIRouter

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {"message": f"Todo added in list {todo_list}"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"message": f"Todo list -- {todo_list}"}