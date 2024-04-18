import tkinter as tk
from tkinter import dialog

root = tk.Tk()
root.title('Mini-bloc')
root.geometry("300x400")
#creation de la menu bar
menu_bar = tk.Menu(root)
#ajouter un menu deroulant appelle fichier au menu bar
Fichier_menu = tk.Menu(menu_bar , tearoff=0) # la fonctionne tearoff empeche le detachment du menu de la menu bar
menu_bar.add_cascade(label="Fichier" , menu=Fichier_menu , activebackground="black" , activeforeground="white" , background="white" , foreground="black")

root.config(menu=menu_bar)
root.mainloop()
