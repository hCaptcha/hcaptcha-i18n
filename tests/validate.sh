#!/bin/sh

find . -not -path './node_modules/*' -type f -name '*.json' | while read json; do echo $json ; jq --exit-status . $json > /dev/null || exit 1; done
