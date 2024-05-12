import tkinter as tk
from tkinter import filedialog 
from tkinter import messagebox

#creer un nouveau fichier
def nouveau():
    texte.delete('1.0' , tk.END)

# ouvrir un fichier 
def ouvrir():
    global current_file
    file_path = filedialog.askopenfilename()
    if file_path:
        current_file = file_path
        with open(file_path , 'r') as file:
            text_area.delete("1.0" , "end")
            text_area.insert("1.0" , file.read())

# enregistre un fichier
    def enregistrer():
    if current_file:
        with open(current_file , 'w') as file:
            file.write(text_area.get("1.0" , "end-1c"))
    else:
        enregistrer_sous()

def enregistrer_sous():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path , "w") as file:
            file.write(text_area.get("1.0" , "end-1c"))
            
def copier_text():
#recupere le texte selectionne dans la zone de texte
    choice_text = text_area.get("1.0" , "end-1c")
#ajoute le texte au presse-papiers
    root.clipboard_clear()
    root.clipboard_append(choice_text)

def coller_text():
#recupere le texte du presse-papiers
    clipboard_text = root.clipboard_get()
#insere le texte dans le widget
    text_area.insert("insert" , clipboard_text)


# declarer la fenetre principale
root = tk.Tk()
root.title('Mini-bloc')
root.geometry("300x400")

# espace de saisi
text_area = tk.Text(root)
text_area.pack(fill="both", expand=True)
text_area.bind("<Control-c>" , copier_text)
text_area.bind("<Control-v>" , coller_text)

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
edition.add_command(label="copier" , command=copier_text)
edition.add_command(label="coller" , command=coller_text)
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
