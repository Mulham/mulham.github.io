# -*- coding: utf-8 -*-
import tech_dict
a = input("Enter word: ")
while a:
	try:
		print("This word exists and it means: ",tech_dict.dict[a][0])
	except:
		tech_dict.dict[a] = [[],[]]
		tech_dict.dict[a][0].append(input("Enter meaning: "))
		tech_dict.dict[a][1].append(input("Enter type: "))
		c = input("Enter other meaning: ")
		while c:
			tech_dict.dict[a][0].append(c)
			tech_dict.dict[a][1].append(input("Enter type: "))
			c = input("Enter next meaning: ")
	a = input("Enter next word: ")
print("Closing ...")
print('Number of words till now: ',len(tech_dict.dict))
b = open("tech_dict.py", encoding="utf-8", mode="w")
b.write("dict = {")
i = 0
for c,d in tech_dict.dict.items():
	i += 1
	b.write('"'+c+'": ['+"\n")
	b.write(str(d[0])+",\n")
	b.write(str(d[1])+",\n")
	if i == len(tech_dict.dict):
		b.write("]}"+"\n")
		break
	b.write("],"+"\n")
b.close()