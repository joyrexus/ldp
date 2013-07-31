SOURCE_DIR=$(today) # dated dir for converting excel files to TSV

mkdir -p "$SOURCE_DIR/excel"
mkdir -p "$SOURCE_DIR/sheets/info"
mkdir -p "$SOURCE_DIR/sheets/transcript"
echo "Put incoming transcripts in $SOURCE_DIR/excel"

sqlite3 "$SOURCE_DIR/data.db" < schema.sql  # temp db for incoming data
