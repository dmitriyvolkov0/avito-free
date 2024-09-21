# Установка
# pip install fastapi[all]
# pip install beautifulsoup4

# Запуск
# uvicorn --host 0.0.0.0 main:app --reload
# uvicorn main:app --reload

# Получить requirements.txt
# pip freeze > requirements.txt

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from functions import get_data_by_request

app = FastAPI()

# @app.get("/")
# async def read_root(request: Request):
#     return RedirectResponse(f"{request.url}docs")

@app.get("/name")
async def get_name():
    return {"name": "Oleg"}

@app.get("/email")
async def get_email():
    return {"email": "Ivanov"}

@app.get("/get-data")
async def get_data(text: str):
    return get_data_by_request(text=text)