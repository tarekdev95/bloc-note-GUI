import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import colorchooser


# fonction de la calculatrice 
formule_init = ""
def calculatrice():
    global formule_init

    # fonction du formule entrée 
    def formule(num):
        global formule_init
        formule_init += str(num)
        valeur.set(formule_init)

    # fonction CE
    def clear_space():
        global formule_init
        formule_init = " "
        valeur.set("0")


    def evaluer():
        try:
            resultat = eval(formule_init)
            valeur.set(resultat)
        except:
            valeur.set("Error")

    #  Fenetre principale de la calculatrice
    clc = tk.Toplevel()
    clc.title("Calculatrice")
    clc.geometry("400x300")
    clc.resizable(width= False, height = False)

    valeur = tk.StringVar()
    # espace des operations
    equation = tk.Entry(clc, textvariable = valeur, font = 30)
    equation.grid(row = 0, columnspan = 4, rowspan = 2, ipady= 10, ipadx = 50)
    clc.rowconfigure(0, weight=1)
    clc.rowconfigure(1, weight=1)
    clc.rowconfigure(2, weight=1)
    clc.rowconfigure(3, weight=1)
    clc.rowconfigure(4, weight=1)
    clc.rowconfigure(5, weight=1)
    clc.columnconfigure(0, weight=1)
    clc.columnconfigure(1, weight=1)
    clc.columnconfigure(2, weight=1)
    clc.columnconfigure(3, weight=1)

    btn1 = tk.Button(clc, text='1', relief='flat', padx = 5, pady = 5, font=20, command=lambda:formule(1))
    btn1.grid(row = 2, column = 0)
    btn2 = tk.Button(clc, text='2', relief='flat', padx = 5, pady = 5, font=20, command=lambda:formule(2))
    btn2.grid(row = 2, column = 1)
    btn3 = tk.Button(clc, text='3', relief='flat', padx = 5, pady = 5, font=20, command=lambda:formule(3))
    btn3.grid(row = 2, column = 2)
    btnp = tk.Button(clc, text = '+',relief = 'flat', padx = 5, pady = 5, font=20, command=lambda:formule('+'))
    btnp.grid(row = 2, column = 3)
    btn4 = tk.Button(clc, text='4', relief='flat', padx = 5, pady = 5, font=20, command=lambda:formule(4))
    btn4.grid(row = 3, column = 0)
    btn5 = tk.Button(clc, text='5', relief='flat', padx = 5, pady = 5, font=20, command=lambda:formule(5))
    btn5.grid(row = 3, column = 1)
    btn6 = tk.Button(clc, text='6', relief='flat', padx = 5, pady = 5, font=20, command=lambda:formule(6))
    btn6.grid(row = 3, column = 2)
    btnsb = tk.Button(clc, text = '-', relief = 'flat', padx = 5, pady = 5, font=20, command=lambda:formule('-'))
    btnsb.grid(row = 3, column = 3)
    btn7 = tk.Button(clc, text='7', relief='flat', padx = 5, pady = 5, font=20, command=lambda:formule(7))
    btn7.grid(row = 4, column = 0)
    btn8 = tk.Button(clc, text='8', relief='flat', padx=5, pady=5, font=20, command=lambda:formule(8))
    btn8.grid(row = 4, column = 1)
    btn9 = tk.Button(clc, text='9', relief='flat', padx=5, pady=5, font=20, command=lambda:formule(9))
    btn9.grid(row = 4, column = 2)
    btnmp = tk.Button(clc, text = '*', relief = 'flat', padx = 5, pady = 5, font=20, command=lambda:formule('*'))
    btnmp.grid(row = 4, column = 3)
    CE = tk.Button(clc, text = 'CE', relief = 'flat', padx = 5, pady = 5, font=20, command=clear_space)
    CE.grid(row = 5, column = 0)
    btnd = tk.Button(clc, text = '/', relief = 'flat', padx = 5, pady = 5, font=20, command=lambda:formule('/'))
    btnd.grid(row = 5, column = 3)
    equal = tk.Button(clc, text = '=', relief = 'flat', padx = 5, pady = 5, font=20, command=evaluer)
    equal.grid(row = 5, column = 1, columnspan=2)

    clc.mainloop()

# ouvrir un fichier 
def ouvrir():
    ouvrir_fichier = filedialog.askopenfilename(title='selectionner un fichier',defaultextension='.txt', filetypes=[('fichier', '*.txt')])
    if ouvrir_fichier is not None:  
        text_area.delete('1.0', tk.END)
        file =  open(ouvrir_fichier, 'r', encoding='utf-8')
        lecture = file.readlines()
        for ligne in lecture:
            text_area.insert(tk.END, ligne)


def color_picker():
    cp = colorchooser.askcolor()
    text_area.tag_add('color_pick', tk.SEL_FIRST, tk.SEL_LAST)
    text_area.tag_config('color_pick', foreground=cp[1])
    
# declarer la fenetre principale
root = tk.Tk()
root.title('Mini-bloc')
root.geometry("600x500")

# espace de saisi
text_area = scrolledtext.ScrolledText(root, )
text_area.pack(fill="both", expand=True)

# Bar de deroulement

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
option.add_command(label="Couleur", command=color_picker)
main_menu.add_cascade(label="Option", menu=option)

# sous menu 4 (outil)
outil = tk.Menu(main_menu, tearoff=0)
outil.add_command(label="Calculatrice", command = calculatrice)
main_menu.add_cascade(label="Outil", menu=outil)



root.config(menu=main_menu)
root.mainloop()
