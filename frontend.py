import tkinter as tk
from tkinter import ttk

agua_manha = 0
agua_tarde = 0
agua_noite = 0
energia_manha = 0
energia_tarde = 0
energia_noite = 0

def receber(a1, a2, a3, e1, e2, e3):
    # Pega os valores
    agua_manha = a1.get()
    agua_tarde = a2.get()
    agua_noite = a3.get()

    energia_manha = e1.get()
    energia_tarde = e2.get()
    energia_noite = e3.get()

    # Mostra no console
    print("Água:", agua_manha, agua_tarde, agua_noite)
    print("Energia:", energia_manha, energia_tarde, energia_noite)

def App():

    def criar_bloco(frame_pai, titulo, cor):
        bloco = tk.Frame(frame_pai, bg=cor, padx=10, pady=10)
        ttk.Label(bloco, text=titulo, font=("Arial", 13, "bold"), background=cor).grid(column=0, row=0, columnspan=3, pady=(0,10))

        ttk.Label(bloco, text="Manhã", background=cor).grid(column=0, row=1)
        ttk.Label(bloco, text="Tarde", background=cor).grid(column=1, row=1)
        ttk.Label(bloco, text="Noite", background=cor).grid(column=2, row=1)

        entrada_manha = ttk.Entry(bloco)
        entrada_tarde = ttk.Entry(bloco)
        entrada_noite = ttk.Entry(bloco)

        entrada_manha.grid(column=0, row=2, padx=5, pady=5)
        entrada_tarde.grid(column=1, row=2, padx=5, pady=5)
        entrada_noite.grid(column=2, row=2, padx=5, pady=5)

        return bloco, entrada_manha, entrada_tarde, entrada_noite

    def dia1():
        root = tk.Tk()
        root.title("Registro Dia 1")

        frm = ttk.Frame(root, padding=20)
        frm.grid()

        ttk.Label(frm, text="Dia 1", font=("Arial", 18, "bold")).grid(column=0, row=0, pady=10)

        # Criar bloco água
        bloco_agua, entrada1Agua, entrada2Agua, entrada3Agua = criar_bloco(frm, "Água", "deepskyblue")
        bloco_agua.grid(column=0, row=1, pady=10)

        # Criar bloco energia
        bloco_energia, entrada1Energia, entrada2Energia, entrada3Energia = criar_bloco(frm, "Energia", "lightgoldenrod")
        bloco_energia.grid(column=0, row=2, pady=10)

        def receber1():
            receber(entrada1Agua, entrada2Agua, entrada3Agua, entrada1Energia, entrada2Energia, entrada3Energia)
            root.destroy()
        
        # Botão enviar
        ttk.Button(frm, text="Enviar", command=receber1).grid(column=0, row=3, pady=20)

        root.mainloop()

    def dia2():
        root = tk.Tk()
        root.title("Registro Dia 2")

        frm = ttk.Frame(root, padding=20)
        frm.grid()

        ttk.Label(frm, text="Dia 2", font=("Arial", 18, "bold")).grid(column=0, row=0, pady=10)

        # Criar bloco água
        bloco_agua, entrada1Agua, entrada2Agua, entrada3Agua = criar_bloco(frm, "Água", "deepskyblue")
        bloco_agua.grid(column=0, row=1, pady=10)

        # Criar bloco energia
        bloco_energia, entrada1Energia, entrada2Energia, entrada3Energia = criar_bloco(frm, "Energia", "lightgoldenrod")
        bloco_energia.grid(column=0, row=2, pady=10)

        def receber1():
            receber(entrada1Agua, entrada2Agua, entrada3Agua, entrada1Energia, entrada2Energia, entrada3Energia)
            root.destroy()
        
        # Botão enviar
        ttk.Button(frm, text="Enviar", command=receber1).grid(column=0, row=3, pady=20)

        root.mainloop()

    def dia3():
        root = tk.Tk()
        root.title("Registro Dia 3")

        frm = ttk.Frame(root, padding=20)
        frm.grid()

        ttk.Label(frm, text="Dia 3", font=("Arial", 18, "bold")).grid(column=0, row=0, pady=10)

        # Criar bloco água
        bloco_agua, entrada1Agua, entrada2Agua, entrada3Agua = criar_bloco(frm, "Água", "deepskyblue")
        bloco_agua.grid(column=0, row=1, pady=10)

        # Criar bloco energia
        bloco_energia, entrada1Energia, entrada2Energia, entrada3Energia = criar_bloco(frm, "Energia", "lightgoldenrod")
        bloco_energia.grid(column=0, row=2, pady=10)

        def receber1():
            receber(entrada1Agua, entrada2Agua, entrada3Agua, entrada1Energia, entrada2Energia, entrada3Energia)
            root.destroy()
        
        # Botão enviar
        ttk.Button(frm, text="Enviar", command=receber1).grid(column=0, row=3, pady=20)

        root.mainloop()

    def dia4():
        root = tk.Tk()
        root.title("Registro Dia 4")

        frm = ttk.Frame(root, padding=20)
        frm.grid()

        ttk.Label(frm, text="Dia 4", font=("Arial", 18, "bold")).grid(column=0, row=0, pady=10)

        # Criar bloco água
        bloco_agua, entrada1Agua, entrada2Agua, entrada3Agua = criar_bloco(frm, "Água", "deepskyblue")
        bloco_agua.grid(column=0, row=1, pady=10)

        # Criar bloco energia
        bloco_energia, entrada1Energia, entrada2Energia, entrada3Energia = criar_bloco(frm, "Energia", "lightgoldenrod")
        bloco_energia.grid(column=0, row=2, pady=10)

        def receber1():
            receber(entrada1Agua, entrada2Agua, entrada3Agua, entrada1Energia, entrada2Energia, entrada3Energia)
            root.destroy()
        
        # Botão enviar
        ttk.Button(frm, text="Enviar", command=receber1).grid(column=0, row=3, pady=20)

        root.mainloop()

    def dia5():
        root = tk.Tk()
        root.title("Registro Dia 5")

        frm = ttk.Frame(root, padding=20)
        frm.grid()

        ttk.Label(frm, text="Dia 5", font=("Arial", 18, "bold")).grid(column=0, row=0, pady=10)

        # Criar bloco água
        bloco_agua, entrada1Agua, entrada2Agua, entrada3Agua = criar_bloco(frm, "Água", "deepskyblue")
        bloco_agua.grid(column=0, row=1, pady=10)

        # Criar bloco energia
        bloco_energia, entrada1Energia, entrada2Energia, entrada3Energia = criar_bloco(frm, "Energia", "lightgoldenrod")
        bloco_energia.grid(column=0, row=2, pady=10)

        def receber1():
            receber(entrada1Agua, entrada2Agua, entrada3Agua, entrada1Energia, entrada2Energia, entrada3Energia)
            root.destroy()
        
        # Botão enviar
        ttk.Button(frm, text="Enviar", command=receber1).grid(column=0, row=3, pady=20)

        root.mainloop()

    def dia6():
        root = tk.Tk()
        root.title("Registro Dia 6")

        frm = ttk.Frame(root, padding=20)
        frm.grid()

        ttk.Label(frm, text="Dia 6", font=("Arial", 18, "bold")).grid(column=0, row=0, pady=10)

        # Criar bloco água
        bloco_agua, entrada1Agua, entrada2Agua, entrada3Agua = criar_bloco(frm, "Água", "deepskyblue")
        bloco_agua.grid(column=0, row=1, pady=10)

        # Criar bloco energia
        bloco_energia, entrada1Energia, entrada2Energia, entrada3Energia = criar_bloco(frm, "Energia", "lightgoldenrod")
        bloco_energia.grid(column=0, row=2, pady=10)

        def receber1():
            receber(entrada1Agua, entrada2Agua, entrada3Agua, entrada1Energia, entrada2Energia, entrada3Energia)
            root.destroy()
        
        # Botão enviar
        ttk.Button(frm, text="Enviar", command=receber1).grid(column=0, row=3, pady=20)

        root.mainloop()

    def dia7():
        root = tk.Tk()
        root.title("Registro Dia 7")

        frm = ttk.Frame(root, padding=20)
        frm.grid()

        ttk.Label(frm, text="Dia 7", font=("Arial", 18, "bold")).grid(column=0, row=0, pady=10)

        # Criar bloco água
        bloco_agua, entrada1Agua, entrada2Agua, entrada3Agua = criar_bloco(frm, "Água", "deepskyblue")
        bloco_agua.grid(column=0, row=1, pady=10)

        # Criar bloco energia
        bloco_energia, entrada1Energia, entrada2Energia, entrada3Energia = criar_bloco(frm, "Energia", "lightgoldenrod")
        bloco_energia.grid(column=0, row=2, pady=10)

        def receber1():
            receber(entrada1Agua, entrada2Agua, entrada3Agua, entrada1Energia, entrada2Energia, entrada3Energia)
            root.destroy()
        
        # Botão enviar
        ttk.Button(frm, text="Enviar", command=receber1).grid(column=0, row=3, pady=20)

        root.mainloop()

    dia1()
    dia2()
    dia3()
    dia4()
    dia5()
    dia6()
    dia7()

App()
