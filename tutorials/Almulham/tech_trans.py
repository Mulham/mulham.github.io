import gi, tech_dict
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
class dict_window(Gtk.Window):		
	def __init__(self):
		Gtk.Window.__init__(self, title="Al-Mulham Translator")
		self.set_size_request(900, 600)
		self.timeout_id = None
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
		self.add(vbox)
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
		self.add(hbox)
		vbox.pack_start(hbox, True, True, 0)
		self.entry = Gtk.TextView()
		self.buffer = Gtk.TextBuffer()
		hbox.pack_start(self.entry, True, True, 0)
		self.entry.set_wrap_mode(True)
		self.entry1 = Gtk.TextView()
		self.buffer1 = Gtk.TextBuffer()
		hbox.pack_start(self.entry1, True, True, 0)

		

		self.button = Gtk.Button(label="ترجم!")
		self.button.connect("clicked", self.on_button_clicked)
		vbox.pack_start(self.button, True, True, 0)
		self.link = Gtk.LinkButton("https://mulham.github.io", "Visit Al-Mulham Homepage")
		vbox.pack_start(self.link, True, True, 0)
		self.entry1.set_editable(False)

	def on_button_clicked(self, widget):
		text = self.entry.get_buffer().get_text()
		self.entry1.set_wrap_mode(True)
		self.textbuffer = self.entry1.get_buffer()
		self.textbuffer.set_text(str(tech_dict.dict[text][0][0]))
		
win = dict_window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()