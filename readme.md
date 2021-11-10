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

##  Non sleeping results

### time tests
cpu -  is the time from start to finish of the call. It is the time from the moment you hit the Enter key until the moment the wget command is completed.

user - amount of CPU time spent in user mode.

system or sys - amount of CPU time spent in kernel mode.

### 100 requests
SYNC_TEST:              0.14s user 0.08s system 5% cpu 4.035 total

ASYNC_TEST:             0.14s user 0.08s system 8% cpu 2.501 total

THIRD_PARTY_ASYNC_TEST: 0.14s user 0.08s system 8% cpu 2.448 total

### 500 requests
SYNC_TEST:              0.17s user 0.14s system 2% cpu 12.684 total

ASYNC_TEST:             0.14s user 0.08s system 6% cpu 3.563 total

THIRD_PARTY_ASYNC_TEST: 0.13s user 0.08s system 8% cpu 2.448 total

### 1000 requests

SYNC:                   0.21s user 0.20s system 1% cpu 23.663 total

ASYNC:                  0.15s user 0.09s system 5% cpu 4.687 total

THIRD_PARTY_ASYNC_TEST: 0.14s user 0.08s system 8% cpu 2.432 total

### 10000

SYNC:                   1.00s user 1.34s system 1% cpu 3:48.72 total

ASYNC:                  0.17s user 0.16s system 1% cpu 26.168 total

THIRD_PARTY_ASYNC_TEST: 0.13s user 0.08s system 8% cpu 2.650 total

