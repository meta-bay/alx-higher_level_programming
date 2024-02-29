#!/bin/bash
# curl body size

content_length=$(curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f 2)
echo "$content_length"

