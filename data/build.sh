#!/usr/sh

DB="ldp.db"
SERVER="joyrexus.spc.uchicago.edu"

if [ -e $DB ]
then
    rm $DB
fi

URL="http://$SERVER/LDP/data/db/latest/ldp.sql.gz"
curl $URL | gunzip -c | sqlite3 $DB
