#!/bin/bash

echo -e "Part 1:\nPrint first line of file\nUse awk to print contents of column \"code\" and count number of codes with _\n"
echo "head -n 1 Annotations.txt"
head -n 1 Annotations.txt
echo
echo "awk '{ print $1 }' Annotations.txt | grep \"_\" | wc -l"
awk '{ print $1 }' Annotations.txt | grep "_" | wc -l
echo
echo -e "Part 2:\nUse the sed command to delete all the lines that have the symbol “_” in them and keep a backup copy of the initial file."
echo "sed -i.bak '/^[^\t]*_.*/d' Annotations.txt"
sed -i.bak '/^[^\t]*_.*/d' Annotations.txt
echo
