import tkinter as tk

formule_init = ""

# fonction du formule entrée 
def formule(num):
    global formule_init
    formule_init += str(num)
    valeur.set(formule_init)

# fonction CE
def clear_space():
    global formule_init
    formule_init = " "
    valeur.set("")


def evaluer():
    try:
        resultat = eval(formule_init)
        valeur.set(resultat)
    except:
        valeur.set("error")
clc = tk.Tk()
clc.geometry("400x400")
clc.title('calculatrice')
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