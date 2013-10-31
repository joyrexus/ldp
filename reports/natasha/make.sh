for i in {1..12}; do 
    echo "generating session $i"
    query.py $i > sessions/$i.xls
done
