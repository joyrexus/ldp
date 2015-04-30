#!/bin/bash

SOURCE_DIR=$1   # $(today)

sqlite3 $SOURCE_DIR/data.db 'select * from utterances' \
    | awk 'NR > 1 { print }'                           \
    | tsv2sql --mode insert --table utterances -       \
    > $SOURCE_DIR/utterances.insert.sql
