from fastapi import HTTPException
import httpx


async def handle_response(url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code)

        data = resp.json()
    return data
