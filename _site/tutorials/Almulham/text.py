import re, m_dict
text = 'power supply'
basic_translation = []
		#i تجميع علامات النص في سلسلة ليتم إضافتها لاحقاً للترجمة كما هي
marks = re.findall('[,;.?!.\)\(]*', text)
		# ينقص هنا النقطتين : وعلامات الاقتباس "" مع العلم أنه البرنامج حالياً لا يفصل علامتين متتاليتين بينهما فراغ
counter = 0
while counter < len(marks):	#حذف القيم الفارغة
	if marks[counter] == '':
		del marks[counter]
	else:
		counter += 1
text = text + ' '		#for فلترة العلامات في آخر الجملة أيضاً
sentences = re.split('[,;.?!.\)\(]*', text)
counter = 0		#for حذف القيم الفارغة ''
while counter < len(sentences):
	if sentences[counter]:
		if sentences[counter] == ' ':
			del sentences[counter]
		else:
			if sentences[counter][0] == ' ':		#حذف الفراغات أول وآخر الجملة
				sentences[counter] = sentences[counter][1:]
			if sentences[counter][-1] == ' ':
				sentences[counter] = sentences[counter][:-1]
			counter += 1
	else:
		del sentences[counter]
		#so at the end we have sentences contains the sentences between the marks in the given text (slef.text) 
		# not working anymore!: and also contain tranitional phrases independntly

		# start searching from combined word in the dict and translating them if found
counter = 0
for sentence in sentences:
	i = 0
	if re.search('(\D)+ \d*(\D)+', sentence):  	#if the sentence not a single word
		sentence = str(sentence[0].lower()) + sentence[1:]	#making first letter after each mark always lower
		words = sentence.split()	#تقسيم الجملة لكلمات
		while i+3 < len(words):		# Searching four words together
			group = ''
			group = words[i] + ' ' + words[i+1] + ' ' + words[i+2] + ' ' + words[i+3]
			try:
				words[i:i+4] = [m_dic.dict[group][0][0]]
			except:
				i += 1
		i = 0
		while i+2 < len(words):		# Searching three words together
			group = ''
			group = words[i] + ' ' + words[i+1] + ' ' + words[i+2]
			try:
				words[i:i+3] = [m_dic.dict[group][0][0]]
			except:
				i += 1
		i = 0
		while i+1 < len(words):		# Searching two words together
			group = ''
			group = words[i] + ' ' + words[i+1]
			try:
				words[i:i+2] = [m_dic.dict[group][0][0]]
			except:
				i += 1
		for word in words:
			basic_translation.append(word)
	else:
		basic_translation.append(sentence)
	try:		#إضافة العلامة الفاصلة كما هي
		basic_translation.append(marks[counter])
	except:
		pass
	counter += 1		
print(basic_translation)	
			
