from fastapi import FastAPI

from apiautomata.routes import echo

app = FastAPI()

app.include_router(echo.router)


@app.get('/')
async def root():
    return {'message': 'Automata API'}
