#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response
url=$1 curl -s -H "X-School-User-Id: 98" "$url"
