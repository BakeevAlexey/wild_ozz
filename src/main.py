from fastapi import FastAPI

from routers import route_pytest

app = FastAPI()

app.include_router(route_pytest)
