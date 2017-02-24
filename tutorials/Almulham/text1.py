import re
text = 'removed'
def past_tense(word):
	'''test if the world is in the past tense'''
	past_tense = 0		#default: it's not past tense
	if word[-1] == 'd':
		word = word[:-1]	#delete the d letter
		try:
			i = m.dict_dict[word][0][0]
			#this word must be verb. let's check this
			word_index = 0
			for t in m.dict_dict[word][1]:
				if t[:3] == 'فعل':
					# yes, it's really a verb
					past_tense = 1
					break
				word_index += 1
		except:
			if word[-1] == 'e':		#so the word ends with 'ed'
				word = word[:-1]
			try:
				i = m.dict_dict[word][0][0]
				#this word must be verb. let's check this
				word_index = 0
				for t in m.dict_dict[word][1]:
					if t[:3] == 'فعل':
						# yes, it's really a verb
						past_tense = 1
						break
					word_index += 1
			except:
				if word[-1] == word[-2]:	#like knitted
					word = word[:-1]
				elif word[-1] == 'i':		#studied
					word = word[:-1] + 'y'
				try:
					i = m.dict_dict[word][0][0]
					#this word must be verb. let's check this
					word_index = 0
					for t in m.dict_dict[word][1]:
						if t[:3] == 'فعل':
							# yes, it's really a verb
							past_tense = 1
							break
						word_index += 1
				except:
					pass
	if past_tense:
		#translate it
		translated = m_dict.dict[word][0][word_index]
		translated = translated[1:]		#delete: حذف الياء من أول الفعل المضارع لتحويله لماض
		if len(translated) > 2: 		#حيث هذا التشكيل لا ينطبق على كلمة مثل يقع
			if translated[0] == 'ُ':		#for كلمة مثل يُطعم
				translated == 'أ' + translated[1:]
			if len(translated) == 4:		#e لكلمة مثل ينقاد، يصطاد، يشتري يرتاح
				translated = 'ا' + translated
			if translated[-1] == 'ي':		#d لكلمة مثل يعصي
				translated = translated[:-1] + 'ى'
			elif translated[-1] == 'و':		#e لكلمة مثل يلهو
				translated = translated[:-1] + 'ا'
			elif translated[-1] == 'ى':		#s لكلمة مثل يبقى ويشقى
				compared = translated[:2] + 'اء'		#f للبحث عن شقاء/بقاء..
				for y,z in m_dict.dict.items():
					o = 0
					while o < len(z[0]):
						if z[0][o] == compared:
							translated = translated[:2] + 'ي'		#e تحويل الألف المقصورة لياء
							o = 100
							break
						o += 1
					if o == 100:
						break
			if translated[-2] == 'و': 		#c إذا كانت كلمة مثل يعود/يقول يجب استبدال الواو بألف
				translated = translated[:-2] + 'ا' + translated[-1]		
			elif translated[-2] == 'ي':		#s كلمة مثل يطيع/يستطيع يجب تحويل الياء لألف
				tanslated = translated[:-2] + 'ا' + translated[-1]
			#if -- إذا كانت الكلمة مُشكّة فيجب تصحيح التشكيل			
				if translated[-2] == 'َ':		#بدّل الفتحة بالكسرة والكسرة بالفتحة
					translated = translated[:-2] + 'ِ' + translated[-1]
				elif translated[-2] == 'ِ':
					translated = translated[:-2] + 'َ' + translated[-1]
		else:		#Y إذا كانت كلمةمثل يرى/يقع
			if translated[-1] == 'ى':
				translated = translated[0] + 'أ' + translated[-1]		#s حيث يرى تصبح رأى
			else:
				translated = 'و' + translated		#s حيث يقع تصبح وقع
				
		return translated
	else:
		return past_tense
past_test = past_tense('removed')
if past_test:
	print(past_test)
	
