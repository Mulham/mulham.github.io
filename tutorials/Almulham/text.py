import re
text = 'asd mk and, kkdsf; kmpwe, however, klaskd or klmasd lkasd.'
marks = re.findall('[,]*[;]*[.]*[?]*[!]*[.]*[\(]*[\)]*', text)
print(marks)
counter = 0
while counter < len(marks):	#حذف القيم الفارغة
	if marks[counter] == '':
		del marks[counter]
	else:
		counter += 1
print (marks)
text = text + ' '		#for فلترة العلامات في آخر الجملة أيضاً
sentences = re.split('[,;.?!.\)\(]*(and|or|as a result|thus|consequently|for example|for instance|in conclusion|in summary|in fact|in addition|moreover|furthermore|in contrast|on the other hand|nevertheless|nonetheless|however|fortunately|surprisingly|interestingly)*', text)
print (sentences)
counter = 0		#for حذف القيم الفارغة ''
while counter < len(sentences):
	print('counter = ', counter)
	print('len = ', len(sentences))
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
	print('counter = ', counter)
	print('len = ', len(sentences))
	print(sentences)
