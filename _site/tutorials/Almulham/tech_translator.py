# -*- coding: utf-8 -*-
from tkinter import *
import tech_dict
def retrieve_input():
    return text_to_translate.get("1.0",'end-1c')
def translate():
	word = retrieve_input()
	result.insert(1.0, tech_dict.dict[word][0])

dict_window = Tk()
dict_window.title("Almulham Dictionary")
dict_window.geometry("700x600")
text_to_translate = Text(dict_window, height=40, width=50)
result = Text(dict_window, height=40, width=50)
translate_button = Button(dict_window, text='Translate!', command = translate)
text_to_translate.grid(row=1, column=1)
result.grid(row=1, column=2)
translate_button.grid(row=2, column=1, sticky= E)
dict_window.mainloop()
