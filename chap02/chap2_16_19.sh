#!/bin/sh
echo 16:
n=`wc -l ../data/popular-names.txt | awk '{print $1}'`
if test `expr $n % $1` -eq 0 ; then
     ln=`expr $n / $1`
else
     ln=`expr $n / $1 + 1`
fi
echo $ln
split -l $ln ../data/popular-names.txt ../data/16_devided_

echo 17:
cut -f 1 ../data/popular-names.txt | sort | uniq

echo 18:
sort -r -k 3 -t $'\t' ../data/popular-names.txt

echo 19:
cut -f 1 ../data/popular-names.txt | sort | uniq -c | sort -r -k 2 -t ' '
