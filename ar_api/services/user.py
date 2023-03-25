import logging

from sqlalchemy import select, exc, and_
from fastapi import status, HTTPException

from .base import BaseService
from ar_api import schemas
from ar_api.db import tables


logger = logging.getLogger(__name__)


class UserService(BaseService):
    async def get_list(self, user_filter):
        return schemas.users.UsersList(
            users=await self._get_list()
        )

    async def _get_list(self) -> list[tables.User]:
        query = select(tables.User)
        users = list(await self.session.scalars(query))
        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return users

    async def get(
            self, *,
            user_id: int
    ) -> tables.User:
        query = select(tables.User)

        if user_id is not None:
            query = query.filter_by(
                user_id=user_id
            )

        user = await self.session.scalar(query)
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user

    async def get_by_name(self, name: str, job_title: str) -> tables.User:
        query = select(tables.User).filter_by(name=name).filter_by(job_title=job_title)

        user = await self.session.scalar(query)
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user

    async def create(
            self,
            user_schema: schemas.users.UserCreate
    ):
        new_user = tables.User(**user_schema.dict())
        try:
            self.session.add(new_user)
            await self.session.commit()
            return new_user
        except exc.IntegrityError:
            await self.session.rollback()
            user = await self.get_by_name(user_schema.name, user_schema.job_title)
            user.coordinates = user_schema.coordinates
            await self.session.commit()
            return user

    async def delete(
            self,
            user_id: int
    ):
        user = await self.get(user_id=user_id)
        await self.session.delete(user)
        await self.session.commit()

