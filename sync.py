from http import client


def request(url: str) -> bytes:
    conn = client.HTTPConnection(url)
    conn.request("GET", "/")
    res = conn.getresponse()

    assert res.status == 200

    return res.read()


data = request("localhost:8000")
print(data.decode("utf-8"))
