SOURCE_DIR=$(today)

sqlite3 $SOURCE_DIR/data.db 'select * from utterances' | 
    tsv2sql --mode insert --table utterances - > $SOURCE_DIR/utterances.insert.sql
