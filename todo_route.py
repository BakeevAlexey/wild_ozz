from fastapi import APIRouter, Path

from model import TodoClass

todo_router = APIRouter()

todo_list = []


# Добавление записей
@todo_router.post("/todo")
async def add_todo(todo: TodoClass) -> dict:
    todo_list.append(todo)
    return {"message": f"Todo added in list {todo_list}"}


# Получение всех записей
@todo_router.get("/todo")
async def retrieve_todos() -> dict | list:
    try:
        a = todo_list
    except IndexError:
        return {"message": "An empty list, add data."}
    return a


# Получение 1 записи
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(...,
                                              title="The ID of the todo to retrieve.",
                                              description="fsdfsdfs")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }

    return {
        "message": "Todo with supplied ID doesn't exist."
    }


# Обновление данных
@todo_router.put("/todo/{todo_id}")
async def update_todo(
        todo_data: TodoClass,
        todo_id: int = Path(..., title="The ID of the todo to be updated")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated success"}

    return {"message": "Todo with supplied ID doesn't exists."}


# Удаление 1 объекта
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int = Path(..., title="The ID of the todo to be updated")) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo delete successfully"
            }

    return {"message": "Todo wint supplied ID doesn't exists"}


@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()

    return {"message": "Todos deletes successfully"}
