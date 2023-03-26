from redis import Redis

from loguru import logger

redisengine = Redis(host='redis', port=6379, decode_responses=True)

