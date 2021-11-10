# O.W.L: Observability Wellness Liaison 


## Raison d'être

We wanted to test hypotheses regarding async python vs running multiple processes. 


## Instructions

```bash
docker build -t nathanmartins/owl-test . 

cd test-server && docker build -t nathanmartins/owl-server . 

docker network create owl

docker run -p 8000:8000 --name owl-server -d --network owl  nathanmartins/owl-server

docker run --rm -e ASYNC_TEST=10 -e URL=owl-server:8000 --network=owl nathanmartins/owl-test
```

##  Results

### time tests
cpu -  is the time from start to finish of the call. It is the time from the moment you hit the Enter key until the moment the wget command is completed.
user - amount of CPU time spent in user mode.
system or sys - amount of CPU time spent in kernel mode.


### 100 requests
ASYNC_TEST: 0.13s user 0.07s system 8% cpu 2.349 total

SYNC_TEST: 0.13s user 0.08s system 9% cpu 2.105 total

### 500 requests
ASYNC_TEST: 0.13s user 0.08s system 7% cpu 2.816 total

SYNC_TEST: 0.14s user 0.10s system 2% cpu 11.290 total


---

