#!/bin/bash
# only status code
curl -sI -w "%{response_code}" -o /dev/null "$1"
