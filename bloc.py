import tkinter as tk
from tkinter import filedialog

# ouvrir un fichier 
def ouvrir():
    text_area.delete('1.0', tk.END)
    ouvrir_fichier = filedialog.askopenfilename(title='selectionner un fichier',defaultextension='.txt', filetypes=[('fichier', '*.txt')])
    if ouvrir_fichier is not None:  
        file =  open(ouvrir_fichier, 'r', encoding='utf-8')
        lecture = file.readlines()
        for ligne in lecture:
            text_area.insert(tk.END, ligne)
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
fichier.add_command(label="ouvrir un fichier", command=ouvrir)
fichier.add_command(label="Enregistrer")
fichier.add_command(label="Enregistrer sous")
fichier.add_command(label="Quitter", command=root.quit)
main_menu.add_cascade(label="fichier", menu=fichier)

# sous menu 2 (editions)
edition = tk.Menu(main_menu, tearoff=0)
edition.add_command(label="copier-coller")
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



root.config(menu=main_menu)
root.mainloop()
