# -*- coding: utf-8 -*-
import m_dict
a = input("Enter word: ")
while a:
	try:
		print("This word exists and it means: ",m_dict.dict[a][0])
	except:
		m_dict.dict[a] = [[],[],[]]
		m_dict.dict[a][0].append(input("Enter meaning: "))
		m_dict.dict[a][1].append(input("Enter type: "))
		m_dict.dict[a][2].append(input("Enter topic: "))
		c = input("Enter other meaning: ")
		while c:
			m_dict.dict[a][0].append(c)
			m_dict.dict[a][1].append(input("Enter type: "))
			m_dict.dict[a][2].append(input("Enter topic: "))
			c = input("Enter next meaning: ")
	a = input("Enter next word: ")
print("Closing ...")
print('Number of words till now: ',len(m_dict.dict))
b = open("m_dict.py", encoding="utf-8", mode="w")
b.write("dict = {")
i = 0
for c,d in m_dict.dict.items():
	i += 1
	b.write('"'+c+'": ['+"\n")
	b.write(str(d[0])+",\n")
	b.write(str(d[1])+",\n")
	b.write(str(d[2])+",\n")
	if i == len(m_dict.dict):
		b.write("]}"+"\n")
		break
	b.write("],"+"\n")
b.close()