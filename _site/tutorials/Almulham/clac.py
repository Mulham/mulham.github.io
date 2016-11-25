
from tkinter import *
from math import *
# مدختسملا هلعفي امدنع اهذاختا بجي يتلا ةكرحلا فيرعت
# : لاخدلا لقحظ ريرحتبي موقي يذلا ةع لاخدلا حاتفم
def evaluer(event):
	chaine.configure(text = "Résultat = " + str(eval(entree.get())))
# ----- يسيئرلا جمانربلا : -----
fenetre = Tk()
entree = Entry(fenetre)
entree.bind("<Return>", evaluer)
chaine = Label(fenetre)
entree.pack()
chaine.pack()
fenetre.mainloop()
