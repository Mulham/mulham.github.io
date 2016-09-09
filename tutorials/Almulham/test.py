# -*- coding: UTF-8 -*-

import m_dict,rearrange,rules,m_translator,re,unittest
class CheckRightWord(unittest.TestCase):
	test_example = [" it's a good play in theatre history",
						" The hell is play out but maybe not!",
						" try to translate play if you can."]
	translation =["إنها مسرحيّة جيّدة في تاريخ المسرح",
							"الجحيم قادم وربما لا!",
							"حاول أن تترجمني إن استطعت."]
	word_translation = ['؟ مسرحيّة  ؟','يلعب','يعزف']
	def test_right_meaning(self):
		''' The translator must choose the right meaning of a given word'''
		i,c = 3,0
		for sentence in self.test_example:
			result = m_translator.translator(sentence)
			self.assertEqual(result, self.word_translation[c])
			c += 1
	def test_whole_translation(self):
		for sentence in self.test_example:
			result = m_translator.translator(sentence)
			self.assertEqual(self.translation[self.test_example.
			index(sentence)], result)
class CheckRules(unittest.TestCase):
	def test_adj(self):
		'''test adjective rules with noun before it'''
		test_example = ["The clever man",
						"The clever woman",
						"stupid people",
						"Two dump men"]
		translation = ['الرجل الذكيّ',
						'المرأة الذكيّة',
						'أ؟ش؟خ؟ا؟ص؟ أغبياء',
						'رجلا؟ن غبيّا؟ن']
		c = 0
		for sentence in test_example:
			result = m_translator.translator(sentence)
			self.assertEqual(result, translation[c])
			c += 1

if __name__ == '__main__':
	unittest.main()