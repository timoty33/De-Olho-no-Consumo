import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

diasSemana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
diasSemanaDividos = ["Segunda M/T", "Segunda T/N", "Terça M/T", "Terça T/N", "Quarta M/T", "Quarta T/N", "Quinta M/T", "Quinta T/N", "Sexta M/T", "Sexta T/N", "Sábado M/T", "Sábado T/N", "Domingo M/T", "Domingo T/N"]
diferencasTotais = [2, 4, 3, 7, 3, 4, 3]

def graficoDiferencaTotalAgua(x, diferencasTotais):
    plt.bar(x, diferencasTotais, color="#7EB6CA", label="Gasto de água por dia", width=0.5)
    plt.plot(x, diferencasTotais, color="#2C5F72", label="Gasto de água por dia", linestyle="--")
    plt.title("Diferenças no aumento de água !")
    plt.xlabel("Dias", fontweight="bold")
    plt.ylabel("Aumento", fontweight="bold")
    plt.legend()
    plt.show()

def graficoDiferencaTotalEnergia(x, diferencasTotais):
    plt.bar(x, diferencasTotais, color="#FFFF66", label="Gasto de enegia por dia", width=0.5)
    plt.plot(x, diferencasTotais, color="#FF9933", label="Gasto de enegia por dia", linestyle="--")
    plt.title("Diferenças no aumento de energia !")
    plt.xlabel("Dias", fontweight="bold")
    plt.ylabel("Aumento", fontweight="bold")
    plt.legend()
    plt.show()

def graficoDiferencasAgua(DSD, diferencasAgua):
    cores = ['#7EB6CA', '#2C5F72']
    cores_barras = [cores[i % 2] for i in range(len(diferencasAgua))]
    legendas = [
        Patch(facecolor='#7EB6CA', label="Manhã/Tarde"),
        Patch(facecolor='#2C5F72', label="Tarde/Noite")
    ]

    posicoes = np.arange(len(DSD)) - 0.6

    plt.figure(figsize=(7, 5))

    plt.bar(posicoes, diferencasAgua, color=cores_barras)
    plt.title("Diferenças dos gastos de água: Manhã/Tarde | Tarde/Noite")
    plt.xlabel("Dias", fontweight="bold")
    plt.ylabel("Diferenças", fontweight="bold")
    plt.legend(handles=legendas)

    plt.xticks(posicoes, DSD, rotation=45)

    plt.tight_layout()
    plt.show()

def dadosGerais(mediaAgua, mediaEnergia, maxEnergia, maxAgua, minEnergia, minAgua):
    fig, ax = plt.subplots()

    ax.axis('off')

    texto = (
        f"Média de gastos de água: {mediaAgua}\n"
        f"Média de gastos com energia: {mediaEnergia}\n"
        f"Máximo de gasto com água: {maxAgua}\n"
        f"Máximo de gasto com energia: {maxEnergia}\n"
        f"Mínimo de gasto com água: {minAgua}\n"
        f"Mínimo de gasto com energia: {minEnergia}"
    )

    ax.text(0.05, 0.95, texto, transform=ax.transAxes,
            fontsize=12, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='gray'))

    plt.title('Resumo dos Dados de Consumo')

    plt.show()

graficoDiferencasAgua(diasSemanaDividos, [1, 2, 1, 3, 2, 2, 3, 1, 2, 4, 1, 4, 2, 1])
