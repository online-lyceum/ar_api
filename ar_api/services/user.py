import logging

from sqlalchemy import select, exc, and_
from fastapi import status, HTTPException

from .base import BaseService
from ar_api import schemas
from ar_api.db import redis_handler


logger = logging.getLogger(__name__)


class UserService(BaseService):
    async def get_list(self, name_filter, job_title_filter):
        if name_filter is None:
            name_filter = ''
        if job_title_filter is None:
            job_title_filter = ''
        users = redis_handler.get_users()
        ret = users
        if name_filter or job_title_filter:
            ret = []
            for user in users:
                if name_filter in user.name and job_title_filter in user.job_title:
                    ret.append(user)
        return schemas.users.UsersList(users=ret)

    async def create(
            self,
            user_schema: schemas.users.UserCreate
    ) -> str:
        return redis_handler.create_user(**user_schema.dict())

