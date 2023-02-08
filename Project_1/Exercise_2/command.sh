#!/bin/bash

echo "All files in the directory:" && ls ~ && echo -n "The number of readeable directories: " && ls -l ~ | grep -e "^dr.*$" | wc -l