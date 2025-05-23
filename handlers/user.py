from typing import Annotated
from fastapi import APIRouter, Depends

from dependency import get_user_service
from schema import UserLoginSchema
from schema.user import UserCreateSchema
from service.user import UserService

router = APIRouter(prefix='/user', tags=['user'])


@router.post('', response_model=UserLoginSchema)
async def create(body: UserCreateSchema, user_service: Annotated[UserService, Depends(get_user_service)]):
    return user_service.create_user(body.username, body.password)
