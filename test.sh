#!/usr/bin/env bash

if [[ -n "${SYNC_TEST}" ]]; then

  for ((i = 0; i < SYNC_TEST; i++)); do
    echo "Iteration $i"
    python3 sync.py &
  done

fi

if [[ -n "${ASYNC_TEST}" ]]; then
  python3 async.py
fi
