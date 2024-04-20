import tkinter as tk
from tkinter import filedialog 
from tkinter import messagebox

#creer un nouveau fichier
def nouveau():
    texte.delete('1.0' , tk.END)

# ouvrir un fichier 
def ouvrir():
    ouvrir_fichier = filedialog.askopenfilename(title='selectionner un fichier',defaultextension='.txt', filetypes=[('fichier', '*.txt')])
    if ouvrir_fichier is not None:  
        text_area.delete('1.0', tk.END)
        file =  open(ouvrir_fichier, 'r', encoding='utf-8')
        lecture = file.readlines()
        for ligne in lecture:
            text_area.insert(tk.END, ligne)

# enregistre un fichier
def enregistre():
    file_name = filedialog.askopenfilename(mode = 'w' , dafaultextension = ".txt")
    if file_name:
        with open(file_name , 'r') as file:
            file_content = file.read()
            text_area.delete('1.0' , tk.END)
            text_area.insert(tk.END , file_content)

# enregistre un fichier en fichier.txt
def enregistrer_sous():
    fichier = filedialog.asksaveasfile(mode='w' , defaultextension=".txt")
    if fichier is None:
        contenu = text.get("1.0" , tk.END)
        with open(fichier , 'r') as file:
            file.read(contenu)
# declarer la fenetre principale
root = tk.Tk()
root.title('Mini-bloc')
root.geometry("300x400")

# espace de saisi
text_area = tk.Text(root)
text_area.pack(fill="both", expand=True)

# menu principale
main_menu = tk.Menu(root)

# sous menu 1 (fichier)
fichier = tk.Menu(main_menu, tearoff=0)
fichier.add_command(label="nouveau fichier" , command=nouveau)
fichier.add_command(label="ouvrir un fichier", command=ouvrir)
fichier.add_command(label="Enregistrer" , command=enregistre)
fichier.add_command(label="Enregistrer sous" , command=enregistrer_sous)
fichier.add_command(label="Quitter", command=root.quit)
main_menu.add_cascade(label="fichier", menu=fichier)

# sous menu 2 (editions)
edition = tk.Menu(main_menu, tearoff=0)
edition.add_command(label="copier")
edition.add_command(label="coller")
main_menu.add_cascade(label="edition", menu=edition)

# Sous menu 3 (Option)
option = tk.Menu(main_menu, tearoff=0)
option.add_command(label="Taille de texte")
option.add_command(label="Couleur")
main_menu.add_cascade(label="Option", menu=option)

# sous menu 4 (outil)
outil = tk.Menu(main_menu, tearoff=0)
outil.add_command(label="Calculatrice")
main_menu.add_cascade(label="Outil", menu=outil)


#nom du fichier pas defaut
file_name = "notes.txt"


root.config(menu=main_menu)
root.mainloop()
