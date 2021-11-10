import os
from http import client


def request(url: str) -> bytes:
    conn = client.HTTPConnection(url)
    conn.request("GET", "/")
    res = conn.getresponse()

    assert res.status == 200

    return res.read()


data = request(os.environ.get("URL"))
print(data.decode("utf-8"))
