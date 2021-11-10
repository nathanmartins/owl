import aiohttp
import asyncio
import os


async def main():

    async with aiohttp.ClientSession() as session:
        r = os.environ.get("ASYNC_TEST")
        if not r:
            r = 10
        for i in range(int(r)):
            print(f"Iteration {i}")
            async with session.get(f'http://{os.environ.get("URL")}') as response:
                assert response.status == 200
                parsed_response = await response.read()
                print(parsed_response)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
