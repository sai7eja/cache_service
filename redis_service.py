import redis.asyncio as redis

async def set_cache(key,value):
	r = await redis.Redis(host = "localhost", port = 8090)
	await r.set(key,value)



