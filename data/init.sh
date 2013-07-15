#!/usr/sh

DB="ldp.db"
VERSION=$(cat VERSION)
SERVER="joyrexus.spc.uchicago.edu"  # for downloading utterance table data

if [ -e $DB ]
then
    rm $DB
fi

# import TSV data file ($path) into table
function import
{
    path=$1
    table=$2
    prefix=${path%%:*}
    extension=${path##*.}
    echo "Importing $path into $table"
    if [ $prefix = http ]
    then
        curl $path | gunzip -c | sed 1d | 
            sqlite3 -separator '	'  $DB ".import /dev/stdin $table"
    elif [ $extension = gz ]
        then
            gunzip -c $path | sed 1d | \
            sqlite3 -separator '	'  $DB ".import /dev/stdin $table"
    else
        sed 1d $path | \
            sqlite3 -separator '	'  $DB ".import /dev/stdin $table"
    fi
}


function read
{
    path=$1
    prefix=${path%%:*}
    extension=${path##*.}
    echo "Reading $path"
    if [ $prefix = http ]
    then
        curl $path | gunzip -c | sqlite3 $DB 
    elif [ $extension = gz ]
        then 
            gunzip -c $path | sqlite3 $DB
    else
        cat $path | sqlite3 $DB
    fi
}


# IMPORT LOCAL TABLES

TABLES="subjects sessions visits transcripts measures"

for table in $TABLES; do
    schema="tables/$table/schema.sql"
    read $schema
    for data in $(ls tables/$table/data*); do
        import $data $table 
    done;
done;


# IMPORT REMOTE TABLES

TABLES="utterances"

for table in $TABLES; do
    URL="http://$SERVER/ldp/data/$table/$VERSION"
    schema="$URL/schema.sql.gz"
    data="$URL/data.tsv.gz" 
    read $schema
    import $data $table
done;


# UPDATE ALL TABLES

for update in $(ls tables/*/updates/$VERSION/*.sql); do
    read $update
done;


# ADD LOG TABLE AND TRIGGERS

read "tables/log/schema.sql"
