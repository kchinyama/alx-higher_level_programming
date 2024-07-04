#!/usr/bin/bash
# demo script that takes url and sends request for size of body

url="$1"

size=$(curl  -w '%{size_request}' -o /dev/null "$url")

echo "$size"
