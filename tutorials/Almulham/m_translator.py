import re,m_dict,rules
given_text = input("Enter the text you want to translate: ")
if not given_text:
	print("Text must NOT be empty")
basic_translation = []
# Searching two words together
i = 0
sentences = given_text.split(','and'.')
for sentence in sentences:
	words = sentence.split()
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
	group = ''
	group = group + words[i] + words[i+1]
	i += 1
	words_translation = []
	try:
		group_translation = m_dict.dict[group][0][0]
		f = 0
		while f<i:
			words_translation.extend(words[f])
			f += 1
		words_translation.extend(group_translation)
		g = i+2
		while g<len(words):
			words_translation.extend(word[g])
			g += 1
	except:
		words_translation.extend(words[i])

## end of Searching two words together	
# detecting word type (verb or noun)
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