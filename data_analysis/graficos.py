import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

diasSemana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
diasSemanaDividos = ["Segunda M/T", "Segunda T/N", "Terça M/T", "Terça T/N", "Quarta M/T", "Quarta T/N", "Quinta M/T", "Quinta T/N", "Sexta M/T", "Sexta T/N", "Sábado M/T", "Sábado T/N", "Domingo M/T", "Domingo T/N"]
diferencasTotais = [2, 4, 3, 7, 3, 4, 3]

import matplotlib.pyplot as plt

def tabelaDadosAgua(dados):
    linhas = ["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5", "Dia 6", "Dia 7"]
    colunas = ["Manhã", "Tarde", "Noite"]
    dadosTabela = [
        [dados[0], dados[1], dados[2]],
        [dados[3], dados[4], dados[5]],
        [dados[6], dados[7], dados[8]],
        [dados[9], dados[10], dados[11]],
        [dados[12], dados[13], dados[14]],
        [dados[15], dados[16], dados[17]],
        [dados[18], dados[19], dados[20]]
    ]

    fig, ax = plt.subplots(figsize=(4, 3))  # Tamanho reduzido
    ax.axis('off')

    tabela = ax.table(cellText=dadosTabela,
                      colLabels=colunas,
                      rowLabels=linhas,
                      loc="center")

    tabela.scale(1, 1.2)  # Ajuste leve

    plt.title("Tabela das contagens do hidrômetro", fontsize=12)

    plt.show()

def tabelaDadosEnergia(dados):
    linhas = ["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5", "Dia 6", "Dia 7"]
    colunas = ["Manhã", "Tarde", "Noite"]
    dadosTabela = [
        [dados[0], dados[1], dados[2]],
        [dados[3], dados[4], dados[5]],
        [dados[6], dados[7], dados[8]],
        [dados[9], dados[10], dados[11]],
        [dados[12], dados[13], dados[14]],
        [dados[15], dados[16], dados[17]],
        [dados[18], dados[19], dados[20]]
    ]

    fig, ax = plt.subplots(figsize=(4, 3))  # Igual ao anterior
    ax.axis('off')

    tabela = ax.table(cellText=dadosTabela,
                      colLabels=colunas,
                      rowLabels=linhas,
                      loc="center")

    tabela.scale(1, 1.2)

    plt.title("Tabela das contagens do relógio de luz", fontsize=12)

    plt.show()

def graficoDiferencaTotal(x, diferencasTotaisAgua, diferencasTotaisEnergia):

    plt.subplot(2, 1, 1)
    plt.bar(x, diferencasTotaisAgua, color="#7EB6CA", label="Gasto de água por dia", width=0.5)
    plt.plot(x, diferencasTotaisAgua, color="#2C5F72", label="Gasto de água por dia", linestyle="dotted")
    plt.title("Diferenças no aumento de água !")
    plt.xlabel("Dias", fontweight="bold")
    plt.ylabel("Aumento de 10 em 10 litros", fontweight="bold")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.bar(x, diferencasTotaisEnergia, color="#FFFF66", label="Gasto de enegia por dia", width=0.5)
    plt.plot(x, diferencasTotaisEnergia, color="#FF9933", label="Gasto de enegia por dia", linestyle="dotted")
    plt.title("Diferenças no aumento de energia !")
    plt.xlabel("Dias", fontweight="bold")
    plt.ylabel("Aumento em Kw/H", fontweight="bold")
    plt.legend()

    plt.tight_layout()
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
    plt.ylabel("Diferenças de 10 em 10 litros", fontweight="bold")
    plt.legend(handles=legendas)

    plt.xticks(posicoes, DSD, rotation=45)

    plt.tight_layout()
    plt.show()

def graficoDiferencasEnergia(DSD, diferencasEnergia):
    cores = ['#FFFF66', '#FF9933']
    cores_barras = [cores[i % 2] for i in range(len(diferencasEnergia))]
    legendas = [
        Patch(facecolor='#FFFF66', label="Manhã/Tarde"),
        Patch(facecolor='#FF9933', label="Tarde/Noite")
    ]

    posicoes = np.arange(len(DSD)) - 0.6

    plt.figure(figsize=(7, 5))

    plt.bar(posicoes, diferencasEnergia, color=cores_barras)
    plt.title("Diferenças dos gastos de energia: Manhã/Tarde | Tarde/Noite")
    plt.xlabel("Dias", fontweight="bold")
    plt.ylabel("Diferenças em Kw/H", fontweight="bold")
    plt.legend(handles=legendas)

    plt.xticks(posicoes, DSD, rotation=45)

    plt.tight_layout()
    plt.show()

def graficoPizza(aguaManha, aguaTarde, energiaManha, energiaTarde):
    valores = [aguaManha, aguaTarde, energiaManha, energiaTarde]
    labels = ["Água Manhã-Tarde", "Água Tarde-Noite", "Energia Manhã-Tarde", "Energia Tarde-Noite"]
    cores = ["#7EB6CA", "#2C5F72", "#FFFF66", "#FF9933"]

    plt.pie(valores, labels=labels, colors=cores, autopct="%1.1f%%")
    plt.title("Gastos da água e energia separados em períodos")
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
            bbox=dict(boxstyle='round', facecolor='#ccc', edgecolor='gray'))

    plt.title('Resumo dos Dados de Consumo')

    plt.show()

if __name__ == "__main__":
    graficoPizza(8, 9, 12, 10)
