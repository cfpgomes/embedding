#!/bin/bash

python3.9 src/ampl/ampl_generator.py

new_ampl=$(ls src/ampl/ -t | head -n1 | sed -e 's/\.ampl$//')

glpsol -m src/ampl/"$new_ampl".ampl -o results/"$new_ampl".out