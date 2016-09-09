import re,m_dict
given_text = input("Enter the text you want to translate: ")
if given_text:
	basic_translation = []
	words = given_text.split()
	i = 0
	for t in words:
		#based on type
		word_type = re.search(m_dict.dict[t][1][i],"فعل")
		if word_type:
			#maybe it's a verb

		else:
			#it's definitly noun

		try:
			basic_translation.append(m_dict.dict[t][0][right_word_number]
		except:
			basic_translation.append(t)


else:
	print("Text must NOT be empty")