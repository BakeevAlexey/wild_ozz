from pydantic import BaseModel


class ItemTodo(BaseModel):
    item: str
    statuses: str


class TodoClass(BaseModel):
    id: int
    item: ItemTodo

    # Можно описать метод в документации (redoc, swagger)
    # Но есть лучше способ через указание полей.
    # Field(examples=["Foo"])
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 123,
                    "item": {
                        "item": "sfds",
                        "statuses": "sfs"
                    }
                }
            ]
        }
    }
