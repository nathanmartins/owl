FROM python:3.7-alpine

RUN apk update && apk add bash

COPY test.sh .
COPY async.py .
COPY sync.py .

CMD [ "./test.sh" ]
