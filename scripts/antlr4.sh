#!/usr/bin/env bash

set -ex;

ANTLR_BIN_DIST_DIRECTORY="/tmp"
ANTLR_PROJECT_DIST_PACKAGE="boltun.engine.grammar.antlr4"
ANTLR_PROJECT_DIST_DIRECTORY="sources/boltun/engine/grammar/antlr4"

download() {
    curl -o ${ANTLR_BIN_DIST_DIRECTORY}/antlr.jar -O https://www.antlr.org/download/antlr-4.7.1-complete.jar
}

run() {
    [ ! -z $1 ] && PYTHON_MAJOR_VERSION=$1 || PYTHON_MAJOR_VERSION=3
    echo "Python major version is ${PYTHON_MAJOR_VERSION}"

    java -Xmx500M -cp "${ANTLR_BIN_DIST_DIRECTORY}/antlr.jar:${CLASSPATH}" org.antlr.v4.Tool \
    -package ${ANTLR_PROJECT_DIST_PACKAGE} \
    -listener -visitor \
    -Dlanguage=Python${PYTHON_MAJOR_VERSION} \
    -lib ${ANTLR_PROJECT_DIST_DIRECTORY} \
    ${ANTLR_PROJECT_DIST_DIRECTORY}/Antlr4Grammar.g4

    tree -L 1 ${ANTLR_PROJECT_DIST_DIRECTORY}
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