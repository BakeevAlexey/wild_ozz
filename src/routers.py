from fastapi import APIRouter, HTTPException


route_pytest = APIRouter()


@route_pytest.get("/first_test")
def first_test_foo():
    return {"1": 2}
