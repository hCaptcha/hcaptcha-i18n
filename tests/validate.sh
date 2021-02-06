#!/bin/sh

# basic validity checks
echo "checking JSON validity"
find . -not -path './node_modules/*' -not  -path './package*' -type f -name '*.json' | while read json; do echo $json ; jq --exit-status . $json > /dev/null || exit 1; done

# key mismatch checks
echo "checking for mismatched keysets, i.e. missing or superfluous keys"
find ./languages -type f -name '*.json' | while read json; do echo $json ; python3 bin/check_expected_keys.py $json || exit 1; done
