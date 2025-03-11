#! /bin/bash
COUNTER=0
NUM_FILES=$(ls | wc -l)
STAGE1=0
for FILE in $(ls);
do COUNTER=$(expr $COUNTER + 1);
firstchars=${FILE:0:9}
if [ $firstchars == "apiCalls-" ]; then
lastchars=${FILE/"$firstchars"/""}
if ! grep -r "$lastchars" "Hashes" &> /dev/null; then
echo "$lastchars size= $(ls -s $FILE)"
rm $FILE
fi
fi
done
