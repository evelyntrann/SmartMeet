import json
from app.core.cache import redis_client

async def get_cache(key: str):
    data = await redis_client.get(key)
    # if there's pre-computed data from redis layer, return here
    # else, we will skip redis cache response and compute the data again
    return json.loads(data) if data else None

async def set_cache(key: str, value, ttl: int = 3600):
    await redis_client.set(key, json,dumps(value), ex=ttl)
