#!/bin/bash

for f in src/ampl/*; do glpsol -m "$f" -o results/"$f".out; done