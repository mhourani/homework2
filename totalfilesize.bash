#!/bin/bash

read size <<< $(ls -lHp | grep -v / | awk '{ total += $5}; END {print total}')


if [ $size -ge 1073741824 ]
then
    human_size=$(awk 'BEGIN {printf "%.3g",'$size'/1073741824}')G
elif [ $size -ge 1048576 ]
then
    human_size=$(awk 'BEGIN {printf "%.3g",'$size'/1048576}')M
elif [ $size -ge 1024 ]
then
    human_size=$(awk 'BEGIN {printf "%.3g",'$size'/1024}')K
fi
if [$human_size>0]
then
    echo Size in bytes is $size or $human_size
else
    echo Size in bytes is $size or $human_size
fi
