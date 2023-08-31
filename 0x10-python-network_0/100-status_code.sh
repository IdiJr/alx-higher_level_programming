#!/bin/bash
# sends a request to a URL passed as an argument, and displays only th estatus code of teh response.
curl -s -o /dev/null -w "%{http_code}" "$1"
