#!/usr/bin/env bash

set -ex;

DIST_DIRECTORY="/tmp"

download() {
    curl -o ${DIST_DIRECTORY}/antlr.jar -O https://www.antlr.org/download/antlr-4.7.1-complete.jar
}

run() {
    [ ! -z $1 ] && PYTHON_MAJOR_VERSION=$1 || PYTHON_MAJOR_VERSION=2
    echo "Python major version is ${PYTHON_MAJOR_VERSION}"

    java -Xmx500M -cp "${DIST_DIRECTORY}/antlr.jar:${CLASSPATH}" org.antlr.v4.Tool \
    -package boltun.engine.grammar.antlr4 \
    -listener -visitor \
    -Dlanguage=Python${PYTHON_MAJOR_VERSION} \
    -lib sources/boltun/engine/grammar/antlr4 \
    sources/boltun/engine/grammar/antlr4/Antlr4Grammar.g4
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