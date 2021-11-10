#!/usr/bin/env bash

if [[ -n "${SYNC_TEST}" ]]; then

  for ((i = 0; i < SYNC_TEST; i++)); do
    echo "Iteration $i"
    python3 sync.py &
  done

  wait

fi

if [[ -n "${ASYNC_TEST}" ]]; then
  python3 async.py
fi

if [[ -n "${THIRD_PARTY_ASYNC_TEST}" ]]; then
  python3 third_party_async.py
fi
