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
		self.text = self.textbuffer.get_text(self.textbuffer.get_start_iter(),self.textbuffer.get_end_iter(),False)
	def on_button_clicked(self, widget):
		self.entry1.set_wrap_mode(True)
		self.textbuffer1.set_text(str(tech_dict.dict[text][0][0]))
		
win = dict_window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

########End of User Interface############

window = dict_window()
basic_translation = []
given_text_marks = [] 		#i تجميع علامات النص في سلسلة ليتم إضافتها لاحقاً للترجمة كما هي
given_text_marks_check = re.findall('[,]*[;]*[.]*[?]*[!]*[.]*[and]*[or]*[as a result]*[thus]*[consequently]*[for example]*[for instance]*[in conclusion]*[in summary]*[in fact]*[in addition]*[moreover]*[furthermore]*[in contrast]*[on the other hand]*[nevertheless]*[nonetheless]*[however]*[fortunately]*[surprisingly]*[interestingly]*', window.text)
# يجب تضمين الأقواس في الفلترة!
for match in given_text_marks_check:	#حذف القيم الفارغة
	if match:
		given_text_marks.extend(match)
window.text = window.text + ' '		#for فلترة العلامات في آخر الجملة أيضاً
sentences = re.split('[,]*[;]*[.]*[?]*[!]*[.]*[and]*[or]*[as a result]*[thus]*[consequently]*[for example]*[for instance]*[in conclusion]*[in summary]*[in fact]*[in addition]*[moreover]*[furthermore]*[in contrast]*[on the other hand]*[nevertheless]*[nonetheless]*[however]*[fortunately]*[surprisingly]*[interestingly]*', window.text)
sentences_1 = []		#for حذف القيم الفارغة ''
for sentence in sentences:
	if sentence:
		if sentence[0] == ' ':		#حذف الفراغات أول وآخر الجملة
			sentence = sentence[1:]
		if sentence[-1] == ' ':
			sentence = sentence[:-1]
		sentences_1.extend(sentence)
#so at the end we have sentences_1 contains the sentences between the marks in the given text (window.text)


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

# Here we need to tell the program if any marks found at the end of the word .. ignore/eliminate it.

# ----- start translating single words -----------	

## 1 detecting word type (verb or noun)
words = basic_translation.split()
for word in words:
	bt1 = []
	mark_search = re.split('[,]*[;]*[.]*[?]*[!]*[.]*$', word)
	if mark_search:
		word = re.sub(mark_search, None, word)
	if m_dict.dict[word]:
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
				bt1.append(m_dict.dict[t][0][right_word_number])
			except:
				bt1.append(t)
		# at the end الكلمات الغير مترجمة يتم عمل الاختبارات التالية عليها
	else:
		bt1.expend(word)

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
