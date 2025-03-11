#! /bin/bash

COUNTER=0
NUM_FILES=$(ls | wc -l)
STAGE1=0
echo "There are $NUM_FILES files"
for FILE in $(ls);
do COUNTER=$(expr $COUNTER + 1);
echo "Handling file number $COUNTER: $FILE"; 
# Stage1: Chekcing File Type
echo "checking file type...";
TYPE=$(file $FILE | grep "Zip")
if [ "$TYPE" ]; then
    STAGE1=1
    echo "OK"
elif [ "$(file $FILE | grep 'JAR')" ]; then # this should be deleted in after training and in production mode
    STAGE1=1
    echo "JAR - OK"
else
    STAGE1=0
    echo "Unrecognized"
fi

# Stage2: Unzipping
if (( STAGE1 == 1 )); then
#    echo "Unzipping...";
#    unzip $FILE -d ${FILE//.apk/} &> /dev/null #means replace .apk with the string after / which is empty here so replace with nothing
# Stage2: Getting fuzzy hash
echo "Getting file size..."
SIZE=$(ls -s $FILE)
python3 -c "size = '''$SIZE'''.split();size=size[0]
with open('dataset.csv', 'a') as o:
    o.write(size+';')"
echo "creating fuzzy hash for the whole app..."
Hash1=$(ssdeep -b $FILE)
# Stage3: call graph
#echo "Creating call graph..."
#GML=${FILE//apk/gml}
#$(androguard cg $FILE -o $GML &> /dev/null) #hide command output
# Stage 4: Hash of CG
#echo "creating fuzzy hash for call graph"
#Hash2=$(ssdeep -b $GML)

# Stage 5: Get Permissions
echo "Extracting Features..."

python3 -c "d= '''$Hash1'''.strip().split(',',3);d = d[2];d = d.split(':',1);d = d[1];from androguard.misc import AnalyzeAPK;a, _, dx = AnalyzeAPK('$FILE');perms=a.get_permissions();declared_permissions=a.get_declared_permissions();pckg = a.get_package();services=a.get_services();recs=a.get_receivers()
for i in range(len(services)):
    services[i]=services[i].replace('pckg','')
for i in range(len(recs)):
    recs[i]=recs[i].replace('pckg','')
op_seq = ''
with open('calls', 'w') as o:
    for method in dx.get_methods():
        if method.is_external():
            continue
        m = method.get_method()
        for idx, ins in m.get_instructions_idx():
            op_seq = op_seq + ' ' + str(ins.get_op_value())
            o.write(str(ins.get_output())+'\n')
with open('dataset.csv', 'a') as o:
    o.write(d+';')
    o.write(str(perms)+';')
    o.write(str(declared_permissions)+';')
    o.write(str(services)+';')
    o.write(str(recs)+';')
    o.write(str(op_seq)+'\n')
with open('Hashes', 'a') as o:
    o.write('''$FILE'''+ ';M\n')" #permissions will be added while each permission in a column and between single quotes ''
echo "Preparing API calls..."
grep -r 'Landroid.*;->.*(' calls | grep -o 'Landroid.*(' | sed 's/.$//' > temp.txt
grep -r 'Ljava.*;->.*(' calls | grep -o 'Ljava.*(' | sed 's/.$//' >> temp.txt
grep -r 'Ljavax.*;->.*(' calls | grep -o 'Ljavax.*(' | sed 's/.$//' >> temp.txt
awk '!x[$0]++' temp.txt > apiCalls-$FILE
echo "Removing unneeded files..."
rm $FILE
rm calls
rm temp.txt
fi
done;

