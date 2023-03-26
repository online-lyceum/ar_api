from fastapi import Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession


class BaseService:
    def __init__(
            self,
            response: Response = Response
    ):
        self.response = response
