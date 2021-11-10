import asyncio
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
    future1 = inner_loop.run_in_executor(None, request, 'localhost:8000')
    response1 = yield from future1
    print(response1.decode())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
