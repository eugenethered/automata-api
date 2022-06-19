from typing import List

from exchangetransformrepo.ExchangeTransform import ExchangeTransform
from exchangetransformrepo.repository.ExchangeTransformRepository import ExchangeTransformRepository
from fastapi import APIRouter

from apiautomata.holder.ItemHolder import ItemHolder

router = APIRouter()


@router.get('/transform/exchange', response_model=List[ExchangeTransform])
async def get_all_exchange_transforms():
    exchange_transform_repository = ItemHolder.get_entity(ExchangeTransformRepository)
    return exchange_transform_repository.retrieve()


@router.put('/transform/exchange')
async def create_exchange_transform(exchange_transform: ExchangeTransform):
    exchange_transform_repository = ItemHolder.get_entity(ExchangeTransformRepository)
    exchange_transform_repository.append(exchange_transform)
    return exchange_transform


@router.delete('/transform/exchange')
async def delete_exchange_transform(exchange_transform: ExchangeTransform):
    exchange_transform_repository = ItemHolder.get_entity(ExchangeTransformRepository)
    exchange_transform_repository.remove(exchange_transform)
    return exchange_transform
