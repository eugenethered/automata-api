from typing import List

from fastapi import APIRouter
from missingrepo.Missing import Missing

from apiautomata.holder.PlainItemHolder import PlainItemHolder

router = APIRouter()


@router.get('/missing', response_model=List[Missing])
async def missing():
    missing_repository = PlainItemHolder.get('missing_repository')
    return missing_repository.retrieve()
