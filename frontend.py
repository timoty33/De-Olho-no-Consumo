from tkinter import *
from tkinter import ttk

def App():

    def dia1():
        root = Tk()
        frm = ttk.Frame(root, padding=20)
        frm.grid()
        ttk.Label(frm, text="Dia 1", font=("Arial 18 bold")).grid(column=1, row=0)
        ttk.Label(frm, text="  ").grid(column=1, row=1)
        ttk.Label(frm, text="Água", font=("Arial 13 bold")).grid(column=0, row=2)
        ttk.Label(frm, text="Manhã").grid(column=0, row=3)
        ttk.Label(frm, text="Tarde").grid(column=1, row=3)
        ttk.Label(frm, text="Noite").grid(column=2, row=3)
        entrada1Agua = ttk.Entry(frm)
        entrada1Agua.grid(column=0, row=4)
        entrada2Agua = ttk.Entry(frm)
        entrada2Agua.grid(column=1, row=4)
        entrada3Agua = ttk.Entry(frm)
        entrada3Agua.grid(column=2, row=4)
        ttk.Label(frm, text="  ").grid(column=1, row=5)
        ttk.Label(frm, text="Energia", font=("Arial 13 bold")).grid(column=0, row=6)
        ttk.Label(frm, text="Manhã").grid(column=0, row=7)
        ttk.Label(frm, text="Tarde").grid(column=1, row=7)
        ttk.Label(frm, text="Noite").grid(column=2, row=7)
        entrada1Energia = ttk.Entry(frm)
        entrada1Energia.grid(column=0, row=8)
        entrada2Energia = ttk.Entry(frm)
        entrada2Energia.grid(column=1, row=8)
        entrada3Energia = ttk.Entry(frm)
        entrada3Energia.grid(column=2, row=8)
        ttk.Label(frm, text="  ").grid(column=3, row=9)
        ttk.Label(frm, text="  ").grid(column=3, row=10)
        ttk.Button(frm, text="Enviar", command=root.destroy).grid(column=2, row=11)
        root.mainloop()

    dia1()

App()