#!/bin/bash

FOLDER_NAME="scenario1_N32_classical"

mkdir -p "src/lp/"$FOLDER_NAME""

for f in src/ampl/"$FOLDER_NAME"/*;
do ff=${f##*/};
echo ${ff%.*};
glpsol --check --wlp "src/lp/"$FOLDER_NAME"/"${ff%.*}".lp" -m "${f}";
done
