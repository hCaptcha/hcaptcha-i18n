#!/bin/sh

find . -not -path './node_modules/*' -type f -name '*.json' | while read json; do echo $json ; jq . $json; done
