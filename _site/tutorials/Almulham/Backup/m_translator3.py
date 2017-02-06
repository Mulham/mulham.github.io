import re, m_dict, rules, gi, tech_dict


###User Interface######
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class dict_window(Gtk.Window):		
	def __init__(self):
		Gtk.Window.__init__(self, title="Al-Mulham Translator")
		self.set_size_request(900, 600)
		self.timeout_id = None
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
		self.add(vbox)
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
		self.add(hbox)
		self.entry = Gtk.TextView()
		self.textbuffer = self.entry.get_buffer()
		hbox.pack_start(self.entry, True, True, 0)
		vbox.pack_start(hbox, True, True, 0)
		self.entry1 = Gtk.TextView()
		self.textbuffer1 = self.entry1.get_buffer()
		self.entry.set_wrap_mode(True)
		hbox.pack_start(self.entry1, True, True, 0)
		
		
		self.textbuffer.set_text("أدخل النص المراد ترجمته هنا")
		self.textbuffer1.set_text("النص المترجم يجب أن يظهر هنا")

		self.button = Gtk.Button(label="ترجم!")
		self.button.connect("clicked", self.on_button_clicked)
		vbox.pack_start(self.button, True, True, 0)
		self.link = Gtk.LinkButton("https://mulham.github.io", "Visit Al-Mulham Homepage")
		vbox.pack_start(self.link, True, True, 0)
		self.entry1.set_editable(False)
		self.entry1.set_cursor_visible(False)
		
	

	def dict_progress(self):
		basic_translation = []
		#i تجميع علامات النص في سلسلة ليتم إضافتها لاحقاً للترجمة كما هي
		marks = re.findall('[,;.?!.\)\(]*', self.text)
		counter = 0
		while counter < len(marks):	#حذف القيم الفارغة
			if marks[counter] == '':
				del marks[counter]
			else:
				counter += 1
		self.text = self.text + ' '		#for فلترة العلامات في آخر الجملة أيضاً
		sentences = re.split('[,;.?!.\)\(]*(and|or|as a result|thus|consequently|for example|for instance|in conclusion|in summary|in fact|in addition|moreover|furthermore|in contrast|on the other hand|nevertheless|nonetheless|however|fortunately|surprisingly|interestingly)*', self.text)
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
		#so at the end we have sentences contains the sentences between the marks in the given text (slef.text) and alo contain tranitional phrases independntly


		# start searching from combined word in the dict and translating them if found
		counter = 0
		for sentence in sentences:
			i = 0
			if re.search('(\D)+ \d*(\D)+', sentence):  	#if the sentence not a single word
				words = sentence.split()	#تقسيم الجملة لكلمات
				while i+3 < len(words):		# Searching four words together
					group = ''
					group = words[i] + words[i+1] + words[i+2] + words[i+3]
					try:
						words[i:i+4] = m_dic.dict[group][0][0]
					except:
						i += 1
				i = 0
				while i+2 < len(words):		# Searching three words together
					group = ''
					group = words[i] + words[i+1] + words[i+2]
					try:
						words[i:i+3] = m_dic.dict[group][0][0]
					except:
						i += 1
				i = 0
				while i+1 < len(words):		# Searching two words together
					group = ''
					group = words[i] + words[i+1]
					try:
						words[i:i+2] = m_dic.dict[group][0][0]
					except:
						i += 1
				for word in words:
					basic_translation.append(word)		
				try:
					basic_translation.append(marks[counter])	#إضافة العلامة الفاصلة كما هي
				except:
					pass
				counter += 1
			else:
				basic_translation.append(sentence)
				if not re.search('(and|or|as a result|thus|consequently|for example|for instance|in conclusion|in summary|in fact|in addition|moreover|furthermore|in contrast|on the other hand|nevertheless|nonetheless|however|fortunately|surprisingly|interestingly)*', sentence):
					try:
						basic_translation.append(marks[counter])
					except:
						pass
			
			
		## end of translating combined words as they are (if exist) in dic	

		# Here we basic translation as this: ['word word', ',', 'word', 'and', 'word', '.']

		# ----- start translating single words -----------	

		## 1 detecting word type (verb or noun)
		t = 0
		bt1 = []
		while t < len(basic_translation):
			
			try:	#if the word exist in the dictionary
				bt1.append(m_dict.dict[basic_translation[t]][0][0])
			except:		#else add the word as it is (in english)
				bt1.append(basic_translation[t])
			t += 1
				# at the end الكلمات الغير مترجمة يتم عمل الاختبارات التالية عليها
		final_trans = ''
		for j in bt1:
			if re.search('[,;.?!.\)\(]+', j):
				final_trans = final_trans[:-1]
			final_trans += j #make the translation as string alternative to list
			final_trans += ' '
		return final_trans
	def on_button_clicked(self, widget):
		self.entry1.set_wrap_mode(True)
		self.text = self.textbuffer.get_text(self.textbuffer.get_start_iter(),self.textbuffer.get_end_iter(),False)
		shit = self.dict_progress()
		self.textbuffer1.set_text(str(shit))
		
		
win = dict_window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

########End of User Interface############







