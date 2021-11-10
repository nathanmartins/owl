import asyncio
import os
from http import client


def request(url: str) -> bytes:
    conn = client.HTTPConnection(url)
    conn.request("GET", "/")
    res = conn.getresponse()

    assert res.status == 200

    return res.read()


@asyncio.coroutine
def main():
    inner_loop = asyncio.get_event_loop()

    r = os.environ.get("ASYNC_TEST")
    if not r:
        r = 10

    for i in range(int(r)):
        print(f"Iteration {i}")
        future1 = inner_loop.run_in_executor(None, request, os.environ.get("URL"))
        response1 = yield from future1
        print(response1.decode())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
