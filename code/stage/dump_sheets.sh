SOURCE_DIR=$(today)

cd $SOURCE_DIR/excel

for t in *xls; do
    echo "dumping sheets from $t"
    xls2tsv --sheet info $t > ../sheets/info/$t
    xls2tsv --sheet transcript $t > ../sheets/transcript/$t
done
