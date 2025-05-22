import json
import os

def carregarJson(caminho):

    diretorio_script = os.path.dirname(os.path.abspath(__file__))

    caminho_completo = os.path.join(diretorio_script, caminho)

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

    return round(aguaTotal/periodoTotal)

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

    return round(energiaTotal/periodoTotal)

dataDias = carregarJson("../data/diferencasAguaEnergia.json")
a = mediaAgua(dataDias)

print(a)
