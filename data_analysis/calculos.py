import json
import os

def carregarJson(nomeArquivo):
    with open(nomeArquivo, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvarJson(dados, nomeArquivo, pastaDestino):

    os.makedirs(pastaDestino, exist_ok=True)

    caminhoCompleto = os.path.join(pastaDestino, nomeArquivo)

    with open(caminhoCompleto, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print(f"Arquivo salvo em {caminhoCompleto}")

def jsonDiferencasAguaEnergia(json):
    data = {}

    for i in range(1, 8):
        data[f"dia{i}"] = {"agua": [], "energia": []}

        # Diferenças de água
        agua = json[f"dia{i}"]["agua"]
        for j in range(1, len(agua)):
            data[f"dia{i}"]["agua"].append(agua[j] - agua[j - 1])

        # Diferenças de energia
        energia = json[f"dia{i}"]["energia"]
        for j in range(1, len(energia)):
            data[f"dia{i}"]["energia"].append(energia[j] - energia[j - 1])

    return data

def diferencasTotalAgua(jsonDiferencas):
    diferencasDiaAgua = []
    for i in range(1, 8):
        diferencasDiaAgua.append(sum(jsonDiferencas["dia"+f"{i}"]["agua"]))

    return diferencasDiaAgua

def diferencasTotalEnergia(jsonDiferencas):
    diferencasDiaEnergia = []
    for i in range(1, 8):
        diferencasDiaEnergia.append(sum(jsonDiferencas["dia"+f"{i}"]["energia"]))

    return diferencasDiaEnergia

def mediaAgua(json):

    aguaTotal = sum(json["dia1"]["agua"])
    aguaTotal += sum(json["dia2"]["agua"])
    aguaTotal += sum(json["dia3"]["agua"])
    aguaTotal += sum(json["dia4"]["agua"])
    aguaTotal += sum(json["dia5"]["agua"])
    aguaTotal += sum(json["dia6"]["agua"])
    aguaTotal += sum(json["dia7"]["agua"])

    periodoTotal = len(json["dia1"]["agua"])
    periodoTotal += len(json["dia2"]["agua"])
    periodoTotal += len(json["dia3"]["agua"])
    periodoTotal += len(json["dia4"]["agua"])
    periodoTotal += len(json["dia5"]["agua"])
    periodoTotal += len(json["dia6"]["agua"])
    periodoTotal += len(json["dia7"]["agua"])

    return f"{(aguaTotal/periodoTotal):.2f}"

def mediaEnergia(json):

    energiaTotal = sum(json["dia1"]["energia"])
    energiaTotal += sum(json["dia2"]["energia"])
    energiaTotal += sum(json["dia3"]["energia"])
    energiaTotal += sum(json["dia4"]["energia"])
    energiaTotal += sum(json["dia5"]["energia"])
    energiaTotal += sum(json["dia6"]["energia"])
    energiaTotal += sum(json["dia7"]["energia"])

    periodoTotal = len(json["dia1"]["energia"])
    periodoTotal += len(json["dia2"]["energia"])
    periodoTotal += len(json["dia3"]["energia"])
    periodoTotal += len(json["dia4"]["energia"])
    periodoTotal += len(json["dia5"]["energia"])
    periodoTotal += len(json["dia6"]["energia"])
    periodoTotal += len(json["dia7"]["energia"])

    return f"{(energiaTotal/periodoTotal):.2f}"

def maxMinEnergia(json):
    maxEnergiaSalvo = float('-inf')  # menor valor possível
    minEnergiaSalvo = float('inf')   # maior valor possível

    for i in range(1, 8):
        somaEnergia = sum(json[f"dia{i}"]["energia"])

        if somaEnergia > maxEnergiaSalvo:
            maxEnergiaSalvo = somaEnergia

        if somaEnergia < minEnergiaSalvo:
            minEnergiaSalvo = somaEnergia

    return maxEnergiaSalvo, minEnergiaSalvo

def maxMinAgua(json):
    maxAguaSalvo = float('-inf')
    minAguaSalvo = float('inf')

    for i in range(1, 8):
        somaAgua = sum(json[f"dia{i}"]["agua"])

        if somaAgua > maxAguaSalvo:
            maxAguaSalvo = somaAgua

        if somaAgua < minAguaSalvo:
            minAguaSalvo = somaAgua

    return maxAguaSalvo, minAguaSalvo

def periodosAguaEnergia(json):

    aguaManhaTarde = 0
    aguaTardeNoite = 0
    energiaManhaTarde = 0
    energiaTardeNoite = 0

    for i in range(1, 8):
        
        aguaManhaTarde += json["dia"+f"{i}"]["agua"][0]
        aguaTardeNoite += json["dia"+f"{i}"]["agua"][1]
        energiaManhaTarde += json["dia"+f"{i}"]["energia"][0]
        energiaTardeNoite += json["dia"+f"{i}"]["energia"][1]

    return aguaManhaTarde, aguaTardeNoite, energiaManhaTarde, energiaTardeNoite

def modificarJsonDiferencasAgua(json):

    dados = []

    for i in range(1, 8):
        for j in range(0, 2):
            dados.append(json["dia"+f"{i}"]["agua"][j])

    return dados

def modificarJsonDiferencasEnergia(json):

    dados = []

    for i in range(1, 8):
        for j in range(0, 2):
            dados.append(json["dia"+f"{i}"]["energia"][j])

    return dados

def modificarJsonAgua(json):

    dados = []

    for i in range(1, 8):
        for j in range(0, 3):
            dados.append(json["dia"+f"{i}"]["agua"][j])

    return dados

def modificarJsonEnergia(json):

    dados = []

    for i in range(1, 8):
        for j in range(0, 3):
            dados.append(json["dia"+f"{i}"]["energia"][j])

    return dados

if __name__ == "__main__":
    dataDias = carregarJson(r"..\\data\\data.json")
    a = modificarJsonAgua(dataDias)

    print(a)
