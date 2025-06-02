import tkinter as tk
from tkinter import ttk

agua_manha = 0
agua_tarde = 0
agua_noite = 0
energia_manha = 0
energia_tarde = 0
energia_noite = 0

final_data = {
    "dia1": {
        "agua": [],
        "energia": []
    },
    "dia2": {
        "agua": [],
        "energia": []
    },
    "dia3": {
        "agua": [],
        "energia": []
    },
    "dia4": {
        "agua": [],
        "energia": []
    },
    "dia5": {
        "agua": [],
        "energia": []
    },
    "dia6": {
        "agua": [],
        "energia": []
    },
    "dia7": {
        "agua": [],
        "energia": []
    }
}

def receber(a1, a2, a3, e1, e2, e3):
    # Pega os valores e retorna
    agua_manha = float(a1.get().replace(",", ".").replace(" ", "."))
    agua_tarde = float(a2.get().replace(",", ".").replace(" ", "."))
    agua_noite = float(a3.get().replace(",", ".").replace(" ", "."))

    energia_manha = float(e1.get().replace(",", ".").replace(" ", "."))
    energia_tarde = float(e2.get().replace(",", ".").replace(" ", "."))
    energia_noite = float(e3.get().replace(",", ".").replace(" ", "."))

    print("Água:", agua_manha, agua_tarde, agua_noite)
    print("Energia:", energia_manha, energia_tarde, energia_noite)

    return agua_manha, agua_tarde, agua_noite, energia_manha, energia_tarde, energia_noite

def converter_get():
    global agua_manha, agua_tarde, agua_noite
    global energia_manha, energia_tarde, energia_noite

    agua_manha = float(agua_manha)
    agua_tarde = float(agua_tarde)
    agua_noite = float(agua_noite)

    energia_manha = float(energia_manha)
    energia_tarde = float(energia_tarde)
    energia_noite = float(energia_noite)

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
            a_manha, a_tarde, a_noite, e_manha, e_tarde, e_noite = receber(
                entrada1Agua, entrada2Agua, entrada3Agua, 
                entrada1Energia, entrada2Energia, entrada3Energia
            )

            final_data["dia1"]["agua"] = [a_manha, a_tarde, a_noite]
            final_data["dia1"]["energia"] = [e_manha, e_tarde, e_noite]

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
            a_manha, a_tarde, a_noite, e_manha, e_tarde, e_noite = receber(
                entrada1Agua, entrada2Agua, entrada3Agua, 
                entrada1Energia, entrada2Energia, entrada3Energia
            )

            final_data["dia2"]["agua"] = [a_manha, a_tarde, a_noite]
            final_data["dia2"]["energia"] = [e_manha, e_tarde, e_noite]

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
            a_manha, a_tarde, a_noite, e_manha, e_tarde, e_noite = receber(
                entrada1Agua, entrada2Agua, entrada3Agua, 
                entrada1Energia, entrada2Energia, entrada3Energia
            )

            final_data["dia3"]["agua"] = [a_manha, a_tarde, a_noite]
            final_data["dia3"]["energia"] = [e_manha, e_tarde, e_noite]

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
            a_manha, a_tarde, a_noite, e_manha, e_tarde, e_noite = receber(
                entrada1Agua, entrada2Agua, entrada3Agua, 
                entrada1Energia, entrada2Energia, entrada3Energia
            )

            final_data["dia4"]["agua"] = [a_manha, a_tarde, a_noite]
            final_data["dia4"]["energia"] = [e_manha, e_tarde, e_noite]

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
            a_manha, a_tarde, a_noite, e_manha, e_tarde, e_noite = receber(
                entrada1Agua, entrada2Agua, entrada3Agua, 
                entrada1Energia, entrada2Energia, entrada3Energia
            )

            final_data["dia5"]["agua"] = [a_manha, a_tarde, a_noite]
            final_data["dia5"]["energia"] = [e_manha, e_tarde, e_noite]

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
            a_manha, a_tarde, a_noite, e_manha, e_tarde, e_noite = receber(
                entrada1Agua, entrada2Agua, entrada3Agua, 
                entrada1Energia, entrada2Energia, entrada3Energia
            )

            final_data["dia6"]["agua"] = [a_manha, a_tarde, a_noite]
            final_data["dia6"]["energia"] = [e_manha, e_tarde, e_noite]

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
            a_manha, a_tarde, a_noite, e_manha, e_tarde, e_noite = receber(
                entrada1Agua, entrada2Agua, entrada3Agua, 
                entrada1Energia, entrada2Energia, entrada3Energia
            )

            final_data["dia7"]["agua"] = [a_manha, a_tarde, a_noite]
            final_data["dia7"]["energia"] = [e_manha, e_tarde, e_noite]

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

    print(final_data)
    return final_data

if __name__ == "__main__":
    App()
