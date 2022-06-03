from fastapi import APIRouter, Depends

router = APIRouter()


async def get_version():
    return '0.0.1'


@router.get('/')
async def index(version: str = Depends(get_version)):
    return {'api': 'Automata API', 'version': version}
