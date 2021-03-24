#!/bin/bash

for f in src/ampl/testingQ/*; do glpsol -m "$f" -o results/testingQ/"$f".out; done