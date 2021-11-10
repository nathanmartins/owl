# O.W.L: Observability Wellness Liaison 


## Raison d'être

We wanted to test hypotheses regarding async python vs running multiple processes. 


## Results


docker build -t nathanmartins/owl-test . 

cd test-server && docker build -t nathanmartins/owl-server . 

docker network create owl

docker run -p 8000:8000 --name owl-server -d --network owl  nathanmartins/owl-server

docker run --rm -e ASYNC_TEST=100 -e URL=owl-server:8000 --network=owl   0.13s user 0.07s system 8% cpu 2.349 total

docker run --rm -e SYNC_TEST=100 -e URL=owl-server:8000 --network=owl   0.13s user 0.08s system 9% cpu 2.105 total

docker run --rm -e ASYNC_TEST=1000 -e URL=owl-server:8000 --network=owl   0.14s user 0.08s system 6% cpu 3.586 total



