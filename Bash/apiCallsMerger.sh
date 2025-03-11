#! /bin/bash
COUNTER=0
NUM_FILES=$(ls | wc -l)
STAGE1=0
echo "There are $NUM_FILES files"
for FILE in $(ls -tr);
do COUNTER=$(expr $COUNTER + 1);
echo "Handling file number $COUNTER: $FILE"; 
firstchars=${FILE:0:9}
if [ $firstchars == "apiCalls-" ]; then
echo "OK";
python3 -c "
lines = []
with open('$FILE') as f:
    lines = f.read().splitlines()
    f.close()
with open('dataset.csv', 'r') as istr:
    with open('dataset1.csv', 'a') as ostr:
        for i, line in enumerate(istr):
            if i+1 ==  $COUNTER:
                line = line.rstrip('\n')
                line += '&'+str(lines)
                print(line, file=ostr)
                break
"
fi
done;
