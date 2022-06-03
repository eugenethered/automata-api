from fastapi import FastAPI

from apiautomata.routes import echo, home

app = FastAPI()

app.include_router(home.router)
app.include_router(echo.router)
