import re, m_dict, rules
given_text = input("Enter the text you want to translate: ")
if not given_text:
	print("Text must NOT be empty")
basic_translation = []
given_text_marks = [] 		#i تجميع علامات النص ليتم إضافتها للترجمة كما هي
given_text_marks_check = re.findall('[,]*[;]*[.]*[?]*[!]*[.]*', given_text)
for match in given_text_marks_check:	#حذف القيم الفارغة
	if match:
		given_text_marks.extend(match)
given_text = given_text + ' '		#for فلترة العلامات في آخر الجملة أيضاً
sentences = re.split('[,]*[;]*[.]*[?]*[!]*[.]*', given_text)
sentences_1 = []		#for حذف القيم الفارغة ''
for sentence in sentences:
	if sentence:
		if sentence[0] == ' ':		#حذف الفراغات أول وآخر الجملة
			sentence = sentence[1:]
		if sentence[-1] == ' ':
			sentence = sentence[:-1]
		sentences_1.extend(sentence)
# start searching form combined word in the dict and translating them if found
marks_counter = 0
for sentence in sentences_1:
	i = 0
	words = sentence.split()	#تقسيم الجملة لكلمات
	while i < len(words):
		while i+3 < len(words):		# Searching four words together
			group = ''
			group = words[i] + words[i+1] + words[i+2] + words[i+3]
			try:
				basic.translation.append(m_dic.dict[group][0][0])
				i += 4
			except:
				basic.translation.append(words[i])
				i += 1
		while i+2 < len(words):		# Searching three words together
			group = ''
			group = words[i] + words[i+1] + words[i+2]
			try:
				basic.translation.append(m_dic.dict[group][0][0])
				i += 3
			except:
				basic.translation.append(words[i])
				i += 1
		while i+1 < len(words):		# Searching two words together
			group = ''
			group = words[i] + words[i+1]
			try:
				basic.translation.append(m_dic.dict[group][0][0])
				i += 2
			except:
				basic.translation.append(words[i])
				i += 1
		basic.translation.append(words[i])		#إضافة الكلمة الأخيرة
		i += 1		#هنا ستنتهي الحلقة مباشرة
	basic.translation.append(given_text_marks[marks_counter])	#إضافة العلامة الفاصلة كما هي
	marks_counter += 1
## end of translating combined words as they are (if exist) in dic	

# ----- start translating single words -----------	

## 1 detecting word type (verb or noun)
words = given_text.split()
i = 0
for t in words:
	#based on type
	word_type = re.search(m_dict.dict[t][1][i],"فعل")
	i += 1
	if word_type:
		#maybe it's a verb

	else:
		#it's definitly noun

## end of detecting word type

	try:
		basic_translation.append(m_dict.dict[t][0][right_word_number])
	except:
		basic_translation.append(t)
# at the end الكلمات الغير مترجمة يتم عمل الاختبارات التالية عليها
# short comparative : يجب أن يكون بالأخير لأنه لن يُترجم في البداية كونه غير موجود في القاموس
sc= rules.short_comparative(words)	# words is الكلمة الأجنبية
if sc:
	basic_translation.append(rules.afdal(m_dict.dict[words][0][short_comparative.i])) 
	#short.comparative.i رقم المعنى الذي يحمل النوع "صفة "

# آخر الشي تكون الترجمة بشكل قامئة نعمل لها join()


	# long comparative
	if words[i] == 'more'
		words[i+1] = rules.long_comparative(words[i+1])
	#some fixes before translation
	if word[i] == 'the' and word [i+1] == 'most'
		i += 1		#add 1 to i to pass the without translation
# when calling long_comparative
	if m_dict.dict[word][1]['i'][0:3] == 'اسم':   # not verb
		if re.search('ة$', m_dict.dict[word][0][i]):
			basic_translation.append(m_dict.dict[word][0][i] + 'ً')	#adding فتحتين ً
		else:
			basic_translation.append(m_dict.dict[word][0][i] + 'اً')
		
## end of when ..