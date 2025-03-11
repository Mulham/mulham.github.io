#! /bin/bash


python3 -c "
import re
with open('dataset.csv', 'r') as istr:
    with open('dataset1.csv', 'a') as ostr:
        for i, line in enumerate(istr):
            line = line.rstrip('\n')
            continu = True
            if (re.search('^\d{1,15}&\d{1,15}&', line)):
                while continu:
                    continu = False
                    print('correcting line '+ str(i+1))
                    line = re.sub('^\d{1,15}&', '', line)
                    if (re.search('^\d{1,15}&\d{1,15}&', line)):
                        continu = True
            print(line, file=ostr)
        ostr.close()
    istr.close()           
"

