FROM python:3.7-alpine

RUN apk update && apk add bash

RUN pip install aiohttp

COPY test.sh .
COPY async.py .
COPY sync.py .
COPY third_party_async.py .

CMD [ "./test.sh" ]
