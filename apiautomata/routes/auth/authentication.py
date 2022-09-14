from coreauth.repository.AuthRepository import AuthRepository
from fastapi import APIRouter
from apiautomata.holder.ItemHolder import ItemHolder

router = APIRouter()


@router.put('/auth/api/key-and-secret', response_model=str)
async def create_auth_api_key_with_secret(key: str, secret: str):
    auth_info = {'API_KEY': key, 'API_SECRET': secret}
    auth_repository = ItemHolder.get_entity(AuthRepository)
    auth_repository.store(auth_info)
    return 'OK'
