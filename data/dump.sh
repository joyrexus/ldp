SERVER="/Library/WebServer/Documents/LDP/data/db"

DATE=`date "+%m-%d-%y"`
TARGET="$SERVER/$DATE"
SOURCE="ldp.db"

mkdir $TARGET
echo "dumping contents of $SOURCE to $TARGET"
sqlite3 $SOURCE '.dump' | gzip -c > $TARGET/ldp.sql.gz
echo "linking $TARGET/ldp.sql.gz to $SERVER/latest/ldp.sql.gz"
ln -fs $TARGET/ldp.sql.gz $SERVER/latest/ldp.sql.gz
