#!/usr/bin/env bash

set -ex;

python -m boltun "Hello, {{ Home || World || Day }} !"
python -m boltun "Welcome, {{ Home || Back }} !"