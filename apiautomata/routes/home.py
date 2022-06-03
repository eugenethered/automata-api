from fastapi import APIRouter

from apiautomata.holder.PlainItemHolder import PlainItemHolder

router = APIRouter()


@router.get('/')
async def index():
    return {'api': 'Automata API', 'version': PlainItemHolder.get('version')}

