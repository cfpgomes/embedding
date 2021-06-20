#!/bin/bash

FOLDER_NAME="WV_N64_B0.5_diversified"

mkdir -p "src/lp/"$FOLDER_NAME""

for f in src/ampl/"$FOLDER_NAME"/*;
do ff=${f##*/};
echo ${ff%.*};
glpsol --check --wlp "src/lp/"$FOLDER_NAME"/"${ff%.*}".lp" -m "${f}";
done
