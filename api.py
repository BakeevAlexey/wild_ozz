from fastapi import FastAPI

from todo_route import todo_router

app = FastAPI()

app.include_router(todo_router)