import logging

from fastapi import APIRouter, Depends, Query

from ar_api import schemas
from ar_api.services.user import UserService


logger = logging.getLogger(__name__)
router = APIRouter(
    prefix='/api/user',
    tags=["Hello"],
)


@router.get('', response_model=schemas.users.UsersList)
async def users_list(name_filter: str = Query(default=None), job_title_filter: str = Query(default=None),
                     service: UserService = Depends(UserService)):
    return await service.get_list(name_filter=name_filter, job_title_filter=job_title_filter)


@router.put('', status_code=201)
async def create_user(user: schemas.users.UserCreate,
                      service: UserService = Depends(UserService)):
    await service.create(user)

