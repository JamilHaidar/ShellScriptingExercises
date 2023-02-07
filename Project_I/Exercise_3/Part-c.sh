#!/bin/bash

if [[ ! $# -eq 1 ]]; then
	echo "Invalid number of arguments. Please provide a valid path."
	exit 1
fi

if [[ ! -f $1 ]]; then
	echo "Please provide a valid path for a file."
	exit 1
fi
echo "The number of entries in $1: $(($(wc -l $1 | cut -f1 -d" ")-1))"
read -p "Please enter a valid directory: " mFile

while [[ ! "$mFile" =~ ^[a-zA-Z]*$ ]] || [ -e $mFile ]; do
	echo "Directory invalid or already exists. Please try again with another directory name."
	read -p "Please enter a valid directory: " mFile
done

mkdir "$mFile"
read -p "Please enter a valid Keyword: " mKeyword
mTitle=$(echo "$mKeyword" | sed 's/ /_/' )
head -n 1 $1 > "$mFile/$mTitle".txt
grep -i "$mKeyword" $1 >> "$mFile/$mTitle".txt
echo -e "Wrote $(($(wc -l "$mFile/$mTitle".txt | cut -f1 -d" ")-1)) lines"