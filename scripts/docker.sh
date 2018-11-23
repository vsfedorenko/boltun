#!/usr/bin/env bash

set -ex;

IMAGE_NAME="meiblorn/boltun"

login() {
    echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" \
        --password-stdin
}

build() {
    docker build -t ${IMAGE_NAME} .
}

push() {
    login
    build

    docker push ${IMAGE_NAME}
}


if declare -f $1 > /dev/null
then
  # call arguments verbatim
  "$@"
else
  # Show a helpful error
  echo "'$1' is not a known function name" >&2
  exit 1
fi