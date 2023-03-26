from dataclasses import dataclass
from enum import Enum
from functools import partial

from fastapi import status, HTTPException, Header, Depends
from ar_api.db.base import redisengine

from hashlib import sha256
from ar_api import schemas


user_exists = lambda user_id: redisengine.hexists(user_id)
get_user_data = lambda user_id: redisengine.hgetall(user_id)
__get_user_id = lambda name, job_title: sha256((name + job_title).encode()).hexdigest()


def create_user(name, job_title, coordinates: str) -> str:
    """
    :return: user_id: str"""
    user_id = __get_user_id(name, job_title)
    with redisengine.pipeline() as pipeline:
        pipeline = pipeline.hmset(user_id, {'name': name, 'job_title': job_title, 'coordinates': coordinates})
        pipeline = pipeline.expire(user_id, 120)
        res = pipeline.execute()
    assert res[1], "Expire not set"
    return user_id


def get_users() -> list[schemas.users.UserCreate]:
    return [schemas.users.UserCreate(**get_user_data(user_id)) for user_id in redisengine.keys()]

