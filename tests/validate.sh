#!/bin/sh
find . -type f -exec jsonlint -q '{}' +
