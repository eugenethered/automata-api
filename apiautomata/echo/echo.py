from coreutility.date_utility import get_utc_timestamp
from fastapi import FastAPI

app = FastAPI()


@app.get('/echo')
async def echo():
    return {'echo': get_utc_timestamp()}
