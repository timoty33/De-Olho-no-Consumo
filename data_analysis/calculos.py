import json
import os

def carregarJson(caminho):

    diretorio_script = os.path.dirname(os.path.abspath(__file__))

    caminho_completo = os.path.join(diretorio_script, r"../"+caminho)

    with open(caminho_completo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados

def salvarJson(dados, nomeArquivo, pastaDestino):

    os.makedirs(pastaDestino, exist_ok=True)

    caminhoCompleto = os.path.join(pastaDestino, nomeArquivo)

    with open(caminhoCompleto, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print(f"Arquivo salvo em {caminhoCompleto}")

def jsonDiferencasAguaEnergia(json):
    data = {}

    for i in range(1, 8):
        dia = f"dia{i}"
        data[dia] = {"agua": [], "energia": []}

        # Diferenças de água
        agua = json[dia]["agua"]
        for j in range(1, len(agua)):
            data[dia]["agua"].append(agua[j] - agua[j - 1])

        # Diferenças de energia
        energia = json[dia]["energia"]
        for j in range(1, len(energia)):
            data[dia]["energia"].append(energia[j] - energia[j - 1])

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

if __name__ == "__main__":
    dataDias = carregarJson("../data/diferencasAguaEnergia.json")
    a = diferencasTotalAgua(dataDias)

    print(a)
