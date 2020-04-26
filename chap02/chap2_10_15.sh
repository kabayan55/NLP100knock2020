#!/bin/sh
echo 10:
wc -l ../data/popular-names.txt
echo 11:
sed -e "s/[[:cntrl:]]/ /g" ../data/popular-names.txt
echo 12:
cut -f 1 ../data/popular-names.txt > ../data/col1.txt
cut -f 2 ../data/popular-names.txt > ../data/col2.txt
echo 13:
paste ../data/col1.txt ../data/col2.txt > ../data/merged.txt
echo 14:
head -n $1 ../data/popular-names.txt
echo 15:
tail -n $2 ../data/popular-names.txt
