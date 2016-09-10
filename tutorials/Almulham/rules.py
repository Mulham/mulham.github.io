import m_dict,re
en_subjects = {'i': 'أنا', 'you': ['أنتم' ،'أنت'], 'he': 'هو', 'she': 'هي', 'it':['هي', 'هو'], 'we': 'نحن', 'they': 'هم'}
en_object = ['me', 'you', 'him', 'her', 'it', 'us', 'them']
en_pronouns_possesive = {'mine': 'لي', 'yours': ['لك', 'لكم'], 'his': 'له', 'hers': 'لها', 'ours': 'لنا', 'theirs': 'لهم'}
en_pronouns_reflexive = {'myself': 'نفسي', 'yourself': 'نفسك', 'himself': 'نفسه', 'herself': 'نفسها', 'itself': ['نفسها','نفسه'], 'ourselves': 'أنفسنا', 'yourselves': 'أنفسكم', 'themselves': 'انفسهم'}
en_demostrative = {'this': ['هذا', 'هذه'], 'that': ['ذلك', 'تلك'], 'these': 'هؤلاء', 'those': 'أولئك'}
en_determiners_possessive = {'my': 'ي', 'his': 'ه', 'her': 'ها', 'its': ['ه', 'ها'], 'ours': 'نا', 'your':['ك', 'كم'], 'thier': ['هم', 'هنّ']}
transition_expression = {'therefore': 'لذلك', 'as a result': 'كنتيجة لذلك', 'thus': 'وبالتالي', 'consequently': 'بناءً على ذلك', 'for example': 'على سبيل المثال', 'for instance': 'على سبيل المثال', 'in conclusion': 'وباختصار', 'in summary': 'وباختصار', 'in fact': 'في الواقع', 'in addition': 'بالإضافة لذلك', 'moreover': 'علاوةُ على ذلك', 'furthermore': 'علاوةً على ذلك', 'in contrast': 'وبالمقابل', 'on the other hand': 'وبالمقابل', 'nevertheless': 'مع ذلك', 'nonetheless': 'مع ذلك', 'however': 'على أية حال', 'fortunately': 'لحسن الحظ', 'surprisingly': 'بشكل مفاجئ', 'interestingly': 'بشكل مدهش'}

#short comparative
def short_comparative(word):
	'''test if the word is short comparative'''
	if re.search('er$', word):
		adj = re.sub('er$', '', word)
	short_comparative.i = 0
	short-comparative = 0
	try:
		adj_test = m_dict.dict[adj][1]
		while i < len(adj_test):
			if m_dict.dict[adj][1]['i'][0:3] == 'صفة':
				short-comparative = 1
				break
			short_comparative.i += 1
	except:
		pass
	return short-comparative

def afdal(word):		# word here must be arabic
	'''if short_comparative() gives 1, convert the arabic word to the appropriate form'''
	if word[2] == 'ي':         #if it's على وزن فعيل
		word = 'أ' + word[0] + word[1] + word[3]
		if word[-1] == 'ّ':		#if it's على وزن ذكيّ
			word = 'أ' + word[0] + word[1] + 'ى'
	elif word[1] == 'ا':		#if it's على وزن فاعل
		word = 'أ' + word[0] + word[2] + word[3]
	elif word[2] == 'ّ':		#if it's على وزن فعّل ، مثل هيّن وليّن
		word =  'أ' + word[0] + word[1] + word[3]
		oon = 'ي' + word[0] + 'و' + word[-1]
		for y,z in m_dict.dict.items():		# if it's على وزن أهون وليس ألين
			for i in z[0]:
				if i == oon:
					word = 'أ' + word[0] + 'وَ' + word[3]
					o = 1
					break
			if o:
				break
	else: 			#if it على وزن فَعَل مثل حسن
		word = 'أ' + word
	if word[-1] == word[-2]:	# if the result was like أحبب أو أجدد
		word = word[0] + word[1] + word[2] + 'ّ'
	return word

def long_comparative(word):
	''' Convert the word after 'more' to the appropriate form '''
	if re.search('nt$', word):
		word = re.sub('t$', 'ce', word)
	elif re.search('ed$', word):
		word = re.sub('ed$', '', word)
	else:
		word = re.sub('$', 'ness', word)
	return word