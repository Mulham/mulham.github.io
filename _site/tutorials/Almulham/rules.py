# rules here are : en_subject, en_object, en_pronouns_possesive, en_pronouns_reflexive, en_demostrative, 
# en_determiners_possessive, transition_expression, past_translation, irregular_past, Past_participle
# short_comporative, afdal, long_comporative, past_tense, we_convert_present, we_convert_past, i_convert_present, i_convert_past, she_convert_present, she_convert_past, they_convert_present, they_convert_past, they_convert_past_or_present
import m_dict,re
en_subjects = {'i': 'أنا', 'you': ['أنت', 'أنتم'], 'he': 'هو', 'she': 'هي', 'it': ['هو', 'هي'], 'we': 'نحن', 'they': 'هم'}
en_object = ['me', 'you', 'him', 'her', 'it', 'us', 'them']
en_pronouns_possesive = {'mine': 'لي', 'yours': ['لك', 'لكم'], 'his': 'له', 'hers': 'لها', 'ours': 'لنا', 'theirs': 'لهم'}
en_pronouns_reflexive = {'myself': 'نفسي', 'yourself': 'نفسك', 'himself': 'نفسه', 'herself': 'نفسها', 'itself': ['نفسها','نفسه'], 'ourselves': 'أنفسنا', 'yourselves': 'أنفسكم', 'themselves': 'انفسهم'}
en_demostrative = {'this': ['هذا', 'هذه'], 'that': ['ذلك', 'تلك'], 'these': 'هؤلاء', 'those': 'أولئك'}
en_determiners_possessive = {'my': 'ي', 'his': 'ه', 'her': 'ها', 'its': ['ه', 'ها'], 'ours': 'نا', 'your':['ك', 'كم'], 'thier': ['هم', 'هنّ']}
transition_expression = {'and': 'و', 'or':'أو', 'therefore': 'لذلك', 'as a result': 'كنتيجة لذلك', 'thus': 'وبالتالي', 'consequently': 'بناءً على ذلك', 'for example': 'على سبيل المثال', 'for instance': 'على سبيل المثال', 'in conclusion': 'وباختصار', 'in summary': 'وباختصار', 'in fact': 'في الواقع',
 'in addition': 'بالإضافة لذلك', 'moreover': 'علاوةُ على ذلك', 'furthermore': 'علاوةً على ذلك', 'in contrast': 'وبالمقابل',
 'on the other hand': 'وبالمقابل', 'nevertheless': 'مع ذلك', 'nonetheless': 'مع ذلك', 'however': 'على أية حال',
 'fortunately': 'لحسن الحظ', 'surprisingly': 'بشكل مفاجئ', 'interestingly': 'بشكل مدهش'}
past_translation = {'abode': ['بقِيَ', 'أقام'], 'arose': ['نَهَضَ', 'ارتفع'], 'awoke': ['استيقظ','أيقظ'], 'backbit': '', 'backslid': '',
 'was': 'كان', 'wast': 'كان','wert': 'كانوا', 'were': 'كانوا', 'bore': ['حملت', 'وَلَدت'], 'bare': '', 'beat': ['ضرب', 'أخفقَ'], 'became': 'أصبح',
 'befell': 'َحَدَث', 'begot': ['سبّبَ', 'أنجبَ'], 'begat': '', 'began': 'بَدَأ', 'beheld': 'شاهَدَ', 'bent': 'انحنى', 'breft': '',
 'besought': 'َالتمس', 'beset': 'أزعَجَ', 'bespoke': '', 'bestrode': '', 'bet': 'راهَنَ', 'betook': ['ذَهَبَ', 'عَمِدَ إلى'],
 'bethought': ['تأمَّلَ', 'تذَكَّرَ'], 'bade': ['أمَرَ', 'دعَى'], 'bid': ['أمَرَ', 'دعَى'], 'bode': ['بقِيَ', 'قاوَمَ'], 'bound': ['ربَطَ', 'قَيَّدَ'], 'bit': ['عضَّ', 'لدَغَ'], 'bled': 'نَزَفَ', 'blent': '',
 'blest': 'بارَكَ', 'blew': ['هبَّ', 'نفَخَ'], 'broke': ['كَسَرَ', 'انكسَرَ'], 'bred': ['ولّدَ', 'وُلِدَ'], 'brought': 'جلَبَ', 'broadcast': 'أذاع', 'browbeat': '',
 'built': 'بنى', 'burnt': ['احترق', 'حرقَ'], 'burst': ['فجَّرَ', 'انفجَرَ'], 'bought': 'اشترى', 'could': 'استطاع', 'cast': 'رمى', 'caught': 'مسَكَ', 'chid': 'وبَّخَ', 'chose': 'اختارَ',
 'clove': 'شقَّ', 'cleft': 'شقَّ', 'clung': ['تماسَكَ', 'التصَقَ'], 'clad': '', 'came': 'أتَى', 'cost': 'كلَّفَ', 'crept': 'زحفَ', 'crew': '',
 'cut': ['قطَعَ', 'جرَحَ'], 'durst': '', 'dealt': ['عامَلَ', 'تعامَلَ'], 'dug': 'حفَرَ', 'did': 'َفعَل', 'drew': ['رسَمَ', 'جرَّ'], 'dreamt': 'حلِمَ', 'drank': 'شرِبَ',
 'drove': 'ساقَ', 'dwelt': 'سكَنَ', 'ate': 'أكَلَ', 'fell': ['سقَطَ', 'وقَعَ'], 'fed': 'أطعَمَ', 'felt': ['لمَسَ', 'أحَسَّ'], 'fought': ['قاتَلَ', 'تشاجرَ'], 'found': ['وجَدَ', 'اكتشَفَ'],
 'fled': 'فرَّ', 'flung': 'قذَفَ بقوّة', 'flew': ['طارَ', 'فرَّ'], 'farbore': '', 'forbade': ['حظَرَ', 'منَعَ'], 'forbad': '', 'forecast': '',
 'forewent': '', 'foreknew': 'عرِفَ مقدّماً', 'foresaw': 'تنبَّأَ', 'foretold': 'تكهَّنَ', 'forgot': 'نسيَ', 'forgave': ['سامَحَ', 'غفَرَ'],
 'forsook': ['تخلَّى عن', 'هجَرَ'], 'forswore': '', 'froze': 'تجمَّدَ', 'gainsaid': '', 'got': 'نالَ', 'gilt': '', 'girt': '',
 'gave': 'أعطى', 'went': 'ذهَبَ', 'ground': 'طحَنَ', 'grew': ['نمى', 'نبَتَ'], 'hamstrung': '', 'hung': 'علَّقَ', 'had': 'ملَكَ', 'hadst': 'ملَكَ',
 'hove': '', 'hewed': '', 'hid': ['خبَّأَ', 'اختبأَ'], 'hit': 'ضَرَبَ', 'held': ['أمسَكَ', 'احتفَظَ'], 'hurt': ['جرَحَ', 'آذى'], 'inlaid': ['طعَّمَ', 'رصَّعَ'], 'kept': ['حمى', 'ظلَّ'],
 'knelt': 'ركَعَ', 'knit': ['حبَكَ', 'قطَّبَ حاجبيه'], 'knew': 'عرفَ','laid': ['يضع', 'باضت'], 'led': ['قادَ', 'أرشَدَ'], 'leant': ['استندَ', 'مالَ'],
 'leapt': 'قفزَ', 'learnt': ['علَّم', 'تعلَّمَ'], 'left': 'غادَرَ', 'lent': 'أقرَضَ', 'let': 'ترَكَ',
 'lay': ['تمَدَّدَ', 'كَذِبَ'], 'lit': ['أشرَقَ', 'اشتعلَ'], 'lost': 'فقَدَ', 'made': ['صنَعَ', 'جعَلَ'], 'meant': 'عنَى', 'met': 'قابلَ', 'misdealt': '', 'misgave': '',
 'mislaid': 'أضاعَ', 'misled': ['ضلَّلَ', 'خدَعَ'], 'misspelt': 'أخطأ في التهجئة', 'misspent': 'بدَّدَ', 'mistook': 'أخطأ', 'misunderstood': 'أساء الفهم', 'mowed': 'حصَدَ', 'outbade': '',
 'outbid': '', 'outdid': ['هزَمَ', 'تغلّبَ على'], 'outwent': '', 'outgrew': '', 'outrode': '', 'outran': '',
 'outshone': '', 'outspread': '', 'outwore': '', 'overbore': '', 'overborne': ['قهَرَ', 'استبدَّ'], 'overcast': 'عتَّمَ', 'overcame': ['قهَرَ', 'أنهَكَ'],
 'overdid': 'بالَغَ', 'overdrew': '', 'overate': '', 'overfed': 'أتخَمَ', 'overgrew': '', 'overhung': '',
 'overlaid': '', 'overleapt': '', 'overlay': '', 'overrode': '', 'overran': ['اجتاحَ', 'تخطَّى'], 'oversaw': ['راقبَ', 'فحَصَ'],
 'overset': '', 'overshot': '', 'overslept': 'استغرَقَ في النوم', 'overspread': '', 'overtook': ['تجاوَزَ', 'فاجأَ'],
 'overthrew': ['هزم', 'دمَّر'], 'partook': ['قاسَمَ', 'شارَكَ'], 'paid': 'دفَعَ', 'put': 'وضَعَ', 'quit': ['غادَرَ', 'كفَّ عن'], 'read': 'قرأَ', 'rebuilt': 'أعاد بناء', 'recast': '', 'redid': 'أعاد عمل',
 'relaid': 'وضَعَ ثانيةً', 'remade': 'صنَعَ ثانيةً', 'rent': ['نزَعَ بعنف', 'مزَّقَ'], 'repaid': ['وفَى', 'ردَّ'], 'retold': 'روى ثانيةً', 'rid': ['خلَّصَ', 'حرَّرَ'], 'rode': 'ركِبَ', 'rang': ['قرَعَ', 'رنَّ'], 'rung': '',
 'rose': ['نهضَ', 'بزغَ'], 'ran': 'شغَّلَ', 'sawed': 'نَشَرَ', 'said': 'قال', 'saw': 'رأى', 'sought': 'بحثَ عن', 'sold': ['باعَ', 'خانَ'], 'sent': 'أرسلَ', 'set': ['جلَسَ', 'وضعَ', 'قرَّرَ'], 'sewed': 'خاطَ',
 'shook': ['هزَّ', 'اهتزَّ'], 'shore': '', 'shed': ['َذرَفَ', 'سفَح'], 'shone': ['تألَّقَ', 'لمعَ'], 'shod': '', 'shot': 'أطلق النار',
 'showed': ['أرى', 'بيَّنَ'], 'shred': '', 'shrank': 'تقلَّصَ',
'shrunk': '', 'shrove': '', 'shut': ['أغلقَ', 'حبسَ'], 'sang': ['غنَّى', 'غرَّدَ'], 'sung': '', 'sank': ['غطَسَ', 'غرِقَ'], 'sunk': '', 'sat': 'جلَسَ',
 'slew': 'ذبَحَ', 'slept': 'نامَ', 'slid': 'انزلقَ', 'slung': '', 'slunk': '', 'slit': 'شقَّ', 'smelt': 'شمَّ', 'smote': 'ضرَبَ بقوّة',
 'smit': '', 'sowed': 'بذَرَ', 'spoke': 'تكَلَّم', 'spake': '', 'sped': 'أسرعَ', 'spelt': 'تهجَّى', 'spent': ['أنفق', 'قضى'], 'spilt': '',
 'spun': ['غزَلَ', 'دار بسرعة'],
 'span': ['غزَلَ', 'دار بسرعة'], 'spat': 'بصَقَ', 'spit': '', 'split': 'شقَّ', 'spoilt': ['أتلَفَ', 'دلَّلَ'], 'spread': ['نشَرَ', 'انتشر'],
 'sprang': ['وثَبَ', 'قفَزَ'], 'stood': ['وقف', 'صمد'],
 'stove': '', 'stole': 'سرَقَ', 'stuck': 'ألصَقَ', 'stung': ['لسَعَ', 'لدَغَ'], 'stank': 'نتنَ', 'stunk': '', 'strode': 'مشى بخُطا واسعة',
 'struck': 'ضرَبَ', 'strung': '', 'strove': 'كافح', 'sunburnt': '', 'swore': 'أقسَمَ', 'sware': '', 'swept': ['كَنَسَ', 'اكتسح'],
 'swam': 'سبِحَ', 'swung': ['أرجَحَ', 'تأرجَحَ'], 'took': ['أخَذَ', 'تطلَّبَ'], 'taught': 'علَّمَ', 'tore': ['مزَّقَ', 'اقتلع'],
 'told': ['روى', 'قصَّ'], 'thought': ['اعتقدَ', 'فكَّرَ'], 'throve': 'ازدهر', 'threw': 'قَذَفَ', 'thrust': ['دفَعَ', 'أقحَمَ', 'طعَنَ'], 'trod': ['وطَأَ', 'سحقَ'], 'unbent': '', 'underbid': '',
 'underwent': ['تحمَّلَ', 'قاسى'], 'undersold': '', 'understood': 'فهِمَ', 'undertook': ['تعهَّدَ', 'تولَّى'], 'underwrote': '', 'undid': '',
 'upset': ['أقلقَ', 'أفسَدَ'], 'woke': ['أيقَظَ', 'استيقَظَ'], 'waylaid': 'كمنَ', 'wore': ['ارتدى', 'أبلَى', 'بَلِيَ'], 'wove': ['نسَجَ', 'حبَكَ'],
 'wed': ['زوَّجَ', 'تزوَّجَ'], 'wedded': ['زوَّجَ', 'تزوَّجَ'], 'wept': 'بكى', 'wet': ['بلَّلَ', 'تبلَّلَ'],  'won': ['فازَ', 'ربِحَ'],
 'wound': ['نفخَ', 'لفَّ', 'التفَّ'],
 'withdrew': ['سحَبَ', 'انسحبَ'], 'withheld': ['كبحَ', 'امتنع عن'], 'withstood': ['قاومَ', 'صَمَدَ'], 'wrought': '', 'wrung': ['عصَرَ', 'لوى'],
 'wrote': ['كتَبَ', 'ألَّفَ'], 'writ': ['كتَبَ', 'ألَّفَ']}
irregular_past = ['abode', 'arose', 'awoke', 'backbit', 'backslid',
 'was', 'wast','wert', 'were', 'bore', 'bare', 'beat', 'became',
 'befell', 'begot', 'begat', 'began', 'beheld', 'bent', 'breft',
 'besought', 'beset', 'bespoke', 'bestrode', 'bet', 'betook',
 'bethought', 'bade', 'bid', 'bode', 'bound', 'bit', 'bled', 'blent',
 'blest', 'blew', 'broke', 'bred', 'brought', 'broadcast', 'browbeat',
 'built', 'burnt', 'burst', 'bought', 'could', 'cast', 'caught', 'chid', 'chose',
 'clove', 'cleft', 'clung', 'clad', 'came', 'cost', 'crept', 'crew',
 'cut', 'durst', 'dealt', 'dug', 'did', 'drew', 'dreamt', 'drank',
 'drove', 'dwelt', 'ate', 'fell', 'fed', 'felt', 'fought', 'found',
 'fled', 'flung', 'flew', 'farbore', 'forbade', 'forbad', 'forecast',
 'forewent', 'foreknew', 'foresaw', 'foretold', 'forgot', 'forgave',
 'forsook', 'forswore', 'froze', 'gainsaid', 'got', 'gilt', 'girt',
 'gave', 'went', 'ground', 'grew', 'hamstrung', 'hung', 'had', 'hadst',
 'hove', 'hewed', 'hid', 'hit', 'held', 'hurt', 'inlaid', 'kept',
 'knelt', 'knit', 'knew','laid', 'led', 'leant', 'leapt', 'learnt', 'left', 'lent', 'let',
 'lay', 'lit', 'lost', 'made', 'meant', 'met', 'misdealt', 'misgave',
 'mislaid', 'misled', 'misspelt', 'misspent', 'mistook', 'misunderstood', 'mowed', 'outbade',
 'outbid', 'outdid', 'outwent', 'outgrew', 'outrode', 'outran',
 'outshone', 'outspread', 'outwore', 'overbore', 'overborne', 'overcast', 'overcame',
 'overdid', 'overdrew', 'overate', 'overfed', 'overgrew', 'overhung',
 'overlaid', 'overleapt', 'overlay', 'overrode', 'overran', 'oversaw',
 'overset', 'overshot', 'overslept', 'overspread', 'overtook',
 'overthrew', 'partook', 'paid', 'put', 'quit', 'read', 'rebuilt', 'redid', 'recast',
 'relaid', 'remade', 'rent', 'repaid', 'retold', 'rid', 'rode', 'rang', 'rung',
 'rose', 'ran', 'sawed', 'said', 'saw', 'sought', 'sold', 'sent', 'set', 'sewed',
 'shook', 'shore', 'shed', 'shone', 'shod', 'shot', 'showed', 'shred', 'shrank',
 'shrunk', 'shrove', 'shut', 'sang', 'sung', 'sank', 'sunk', 'sat',
 'slew', 'slept', 'slid', 'slung', 'slunk', 'slit', 'smelt', 'smote',
 'smit', 'sowed', 'spoke', 'spake', 'sped', 'spelt', 'spent', 'spilt', 'spun',
 'span', 'spat', 'spit', 'split', 'spoilt', 'spread', 'sprang', 'stood',
 'stove', 'stole', 'stuck', 'stung', 'stank', 'stunk', 'strode',
 'struck', 'strung', 'strove', 'sunburnt', 'swore', 'sware', 'swept',
 'swam', 'swung', 'took', 'taught', 'tore', 'told', 'thought', 'throve', 'threw', 'thrust', 'trod', 'unbent', 'underbid', 'underwent', 'undersold', 'understood', 'undertook', 'underwrote', 'undid', 'upset', 'woke', 'waylaid', 'wore', 'wove', 'wed', 'wedded', 'wept', 'wet', 'won', 'wound', 'withdrew', 'withheld', 'withstood', 'wrought', 'wrung', 'wrote', 'writ']
past_participle = ['abode', 'arisen', 'awoke',
 'backbitten', 'backbit', 'backslid', 'backslidden',
 'been', 'borne', 'born', 'beaten', 'become', 'befallen',
 'begotten', 'begun', 'beheld', 'bent', 'bereft',
 'besought', 'beset', 'bespoken', 'bespoke', 'bestridden',
 'bestrid', 'bestrode', 'bet', 'betaken', 'bethought',
 'bidden', 'bid', 'bound', 'bitten', 'bit', 'bled',
 'blent', 'blest', 'blown', 'broken', 'broke', 'bred',
 'brought', 'broadcast', 'browbeaten', 'built', 'burnt',
 'burst', 'bought', 'could', 'cast', 'caught', 'chidden', 'chid',
 'chosen', 'cloven', 'cleft', 'clung', 'clothed', 'clad',
 'come', 'cost', 'crept', 'crowed', 'cut', 'dared',
 'dealt', 'dug', 'done', 'drawn', 'dreamt', 'drunk',
 'driven', 'dwelt', 'eaten', 'fallen', 'fed', 'felt',
 'fought', 'found', 'fled', 'flung', 'flown', 'forborne',
 'forbidden', 'forecast', 'foregone', 'foreknown',
 'foreseen', 'foretold', 'forgotten', 'forgiven',
 'forsaken', 'forsworn', 'frozen', 'gainsaid', 'got',
 'gotten', 'girt', 'given', 'gone', 'graven', 'ground',
 'grown', 'hamstrung', 'hung', 'had', 'hove', 'hewn',
 'hidden', 'hid', 'hit', 'held', 'hurt', 'inlaid', 'kept',
 'knelt', 'knit', 'known', 'laden', 'laid', 'led',
 'leant', 'leapt', 'learnt', 'left', 'lent', 'let',
 'lain', 'lit', 'lost', 'made', 'meant', 'met', 'molten',
 'misdealt', 'misgiven', 'mislaid', 'misled', 'misspelt', 'misspent', 'mistaken',
 'misunderstood', 'mown', 'outbidden', 'outbid',
 'outdone', 'outgone', 'outgrown', 'outridden', 'outrun',
 'outshone', 'outspread', 'outworn', 'overborne', 'overborne',
 'overcast', 'overcome', 'overdone', 'overdrawn',
 'overeaten', 'overfed', 'overgrown', 'overhung',
 'overlaid', 'overleapt', 'overlain', 'overridden',
 'overrun', 'overseen', 'overset', 'overshot',
 'overslept', 'overspread', 'overtaken', 'overthrown',
 'overwrought', 'partaken', 'paid', 'put', 'quit', 'read',
 'rebuilt', 'redid', 'recast', 'relaid', 'remade', 'rent', 'repaid',
 'retold', 'rid', 'ridden', 'rung', 'risen', 'riven',
 'run', 'sawn', 'said', 'seen', 'sought', 'sold', 'sent',
 'set', 'sewn', 'shaken', 'shorn', 'shod', 'shot',
 'shown', 'shred', 'shrunk', 'shrunken', 'shriven',
 'shut', 'sung', 'sunk', 'sunken', 'sat', 'slain',
 'slept', 'slid', 'slidden', 'slung', 'slunk', 'slit',
 'smelt', 'smitten', 'smit', 'sown', 'spoken', 'sped',
 'spelt', 'spent', 'split', 'spun', 'spat', 'spit',
 'split', 'spoilt', 'spread', 'sprung', 'stood', 'stove',
 'stolen', 'stuck', 'stung', 'stunk', 'strewn',
 'stridden', 'strid', 'struck', 'stricken', 'strung',
 'striven', 'sunburnt', 'sworn', 'swept', 'swollen',
 'swum', 'swung', 'taken', 'taught', 'torn', 'told', 'thought', 'thriven', 'thrown', 'thrust', 'trodden', 'trod', 'unbent', 'underbidden', 'underbid', 'undergone', 'undersold', 'understood', 'undertaken', 'underwritten', 'undone', 'upset', 'woken', 'woke', 'waylaid', 'worn', 'woven', 'wove', 'wed', 'wept', 'wet', 'won', 'wound', 'withdrawn', 'withheld', 'withstood', 'wrought', 'wrung', 'written', 'writ'] 


#short comparative
def short_comparative(word):
	'''test if the word is short comparative'''
	if re.search('er$', word):
		adj = re.sub('er$', '', word)
	short_comparative.i = 0
	short_comp = 0
	try:
		adj_test = m_dict.dict[adj][1]
		while short_comparative.i < len(adj_test):
			if m_dict.dict[adj][1][i][0:3] == 'صفة':
				short_comp = 1
				break
			short_comparative.i += 1
	except:
		pass
	return short_comp

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

def past_tense(word):
	'''test if the world is in the past tense'''
	past_tense = 0		#default: it's not past tense
	if word[-1] == 'd':
		word = word[:-1]	#delete the d letter
		try:
			i = m_dict.dict[word][0][0]
			#this word must be verb. let's check this
			word_index = 0
			for t in m_dict.dict[word][1]:
				if t[:3] == 'فعل':
					# yes, it's really a verb
					past_tense = 1
					break
				word_index += 1
		except:
			if word[-1] == 'e':		#so the word ends with 'ed'
				word = word[:-1]
			try:
				i = m_dict.dict[word][0][0]
				#this word must be verb. let's check this
				word_index = 0
				for t in m_dict.dict[word][1]:
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
					i = m_dict.dict[word][0][0]
					#this word must be verb. let's check this
					word_index = 0
					for t in m_dict.dict[word][1]:
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
				translated = translated[:-2] + 'ا' + translated[-1]
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
				
def we_convert_present(verb_in_present):		#verb must be in arabic
	''' Convert تحويل الفعل المضارع المسبوق بنحن ليتناسب مع العربية'''
	verb_in_present = 'ن' + verb_in_present[1:]		# حذف ياء المضارع واستبدالها بالنون
	return verb_in_present

def we_convert_past(verb_in_past):		#verb must be in arabic
	'''Convert تحويل الفعل الماض المسبوق بنحن ليتناسب مع العربية'''
	if verb_in_past[-2] == 'ا':		#s مثل عاد أو انقاد
		verb_in_past = verb_in_past[:-2] + verb_in_past[-1]		#s حذف الألف
	verb_in_past = verb_in_past + 'نا'
	return verb_in_past

def i_convert_past(verb_in_past):
	'''s تحويل الفعل الماضي المسبوق بأنا بما يناسب العربية'''
	verb_in_past = verb_in_past + 'تُ'
	return verb_in_past

def i_convert_present(verb_in_present):
	'''s تحويل الفعل المضارع المسبوق بأنا بما يناسب العربية'''
	verb_in_present = 'أ' + verb_in_present[1:]		# حذف ياء المضارع واستبدالها بالألف
	return verb_in_present

def she_convert_present(verb_in_present):
	''' convert present verb led by she or it المؤنث to fit into arabic'''
	verb_in_present = 'ت' + verb_in_present[1:]		# حذف ياء المضارع واستبدالها بالتاء
	return verb_in_present

def she_convert_past(verb_in_past):
	''' convert past verb led by she or it المؤنث to fit into arabic'''
	verb_in_past = verb_in_past + 'تْ'
	return verb_in_past

def they_convert_past(verb_in_past):
	''' convert past verb led by they  جمع المذكر to fit into arabic'''
	if verb_in_past[-1] == 'َ':
		verb_in_past == verb_in_past[:-1]
	verb_in_past = verb_in_past + 'وا'
	return verb_in_past

def they_convert_past_or_present(verb):
	''' convert past or present verb led by they  جمع المؤنث to fit into arabic'''
	if verb[-1] == 'َ' or verb == 'ُ':
		verb == verb[:-1]
	verb = verb + 'نَ'
	return verb

def they_convert_present(verb_in_present):
	''' convert present verb led by they  جمع المذكر to fit into arabic'''
	verb_in_present = verb_in_present + 'ون'
	return verb_in_present

#####################################################
# below is the final and advance level of translating

def damir_uygun(verb, list):
	''' convert arabic verb in present tense damir gore, list elements must be words not sentences! '''
	i = list.index(verb)
	if list[i+1] == 'أنتَ':
		verb = verb[1:] #where verb[0] must b ي like يكون
		verb1 = 'ت' + verb 
		del list[i:i+2]		#delete both verb and pronoun
		list.insert(i, verb1)	#insert the verb in the same position
	elif list[i+1] == 'هم':
		verb = verb + 'وا'	#يكونوا
		del list[i:i+2]		#delete both verb and pronoun
		list.insert(i, verb)	#insert the verb in the same position
		return list

def arabic_marks(list):
	''' make marks suitable to arabic '''
	for i in list:	
		if '?' in i:
			list[list.index(i)] = i.replace('?', '؟')
		if ',' in i:
			list[list.index(i)] = i.replace(',', '،')
	return list
# fn_key = 1
def kaif(how, list):
	''' if found How '''
	how_index = list.index(how)
	if list[how_index + 1] == 'تكون':
		list[how_index + 1] = 'حالك'
	elif list[how_index + 1] == 'يكونوا':
		list[how_index + 1] = 'حالهم'
	return list
def afdal_test(word):	#word in arabic
	''' test if the arabic word is اسم تفضيل '''
	if word[0] == 'أ' and len(word) == 4:
		return True
	else:
		return False
	
def plural(word):
	''' if s detected at the end of the word then tests are here to get sure '''
	if word[-2] == 'e' and re.search('[hsxz]', word[-3]):
		word = word[:-2]	#delete es
	elif word[-2] == 'e' and word[-3] == 'i':
		word = word[:-3] + 'y'	#delete ies and replace it with y
	else:
		word = word[:-1]	#just delete s and hope for the best!
	ok = 0
	try:
		translated = m_dict.dict[word][0][0]
		# Now we must convert the translation to the plural ..
		#جميع مافي الأسفل يحولوا لجمع في حالة الرفع، ويجب التحديد والتعديل لاحقاً
########################جمع المذكر السالم##############################################3
		if afdal_test(translated):	#أسماء التفضيل تجمع دائماً جمع مذكر سالم
			translated = translated[:-1] + 'ون'
			ok = 1
		elif len(trnaslated) > 3 and translated[-1] != 'ة':	#أعتقد جمع المذكر مفرده لا يقل عن أربعة أحرف
			if m_dict.dict[word][1][0] == 'اسم:شخص' or m_dict.dict[word][1][0] == 'صفة:شخص':
				if translated[-1] == 'ى':	#مصطفى => مصطفَوْن
					translated = translated[:-1] + 'َوْن'
				elif translated[-1] == 'ي':	#محامي => محامون
					translated = translated[:-1] + 'ون'
				else:
					translated += 'ون'	# جمع مذكر سالم
				ok = 1
##################################################################################
######################جمع المؤنث السالم####################################
		if ok == 0:	#havn't find a plural yet..
			if translated[-2:] == 'اة':	#فتاة
				translated = translated[:-2] + 'يات'
			elif translated[-1] == 'ة':	#عالمة
				translated = translated[:-1] + 'ات'
			elif transalted[-1] == 'ى':	#هدى/مستشفى
				translated = translated[:-1] + 'يات'
			elif translated[-1] == 'ا':	#d رضا => رضوات
				translated = translated[:-1] + 'وات'
			elif translated[-1] == 'ء':
				if translated[2] == 'ّ': 	#وضّاء
					translated += 'ات'
				else:	#عذراء حسناء الألف للتأنيث
					translated = translated[:-1] + 'وات'
			elif translated[4:] == 'ابن ':
				translated = 'بنات ' + translated[4:]
			elif translated[3:] == 'ذو ':
				translated = 'ذوات ' + translated[3:]
			elif translated == 'أم':
				translated = 'أمهات'
			else:	#هند سعاد زينب
				translated += 'ات'
		return translated
	except:
		return False

def rearrange(list):
	''' re-arrange the sentences and words to suit the arabic structure, the list here contains english words '''
	

