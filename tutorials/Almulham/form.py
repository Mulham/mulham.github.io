import m_dict,re
b = open("new",encoding="utf-8", mode='w')
b.write("dict = {")
i = 0
for c,d in m_dict.dict.items():
	i += 1
	b.write("'"+c+"': ["+"\n")
	b.write(str(d[0])+",\n")
	b.write(str(d[1])+",\n")
	b.write(str(d[2])+",\n")
	if i == len(m_dict.dict):
		b.write("]}"+"\n")
		break
	b.write("],"+"\n")
b.close()
