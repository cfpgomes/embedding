#!/bin/bash

FOLDER_NAME="N64_B0.5_industry_correlated_classical"

mkdir -p "src/lp/"$FOLDER_NAME""

for f in src/ampl/"$FOLDER_NAME"/*;
do ff=${f##*/};
echo ${ff%.*};
glpsol --check --wlp "src/lp/"$FOLDER_NAME"/"${ff%.*}".lp" -m "${f}";
done
