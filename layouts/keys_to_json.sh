#!/bin/bash

keyfile=$1

echo $1

for key in $(cat $1); do
    echo "\"$key\" : {"
#    echo "    \"cols\" : [0],"
    echo "    \"rows\" : [0]"
    echo "},"
done
