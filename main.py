import data_analysis.calculos as dtanC
import data_analysis.graficos as dtanG
import frontend

dataInicial = frontend.App()

diasSemana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
diasSemanaDividos = ["Segunda M/T", "Segunda T/N", "Terça M/T", "Terça T/N", "Quarta M/T", "Quarta T/N", "Quinta M/T", "Quinta T/N", "Sexta M/T", "Sexta T/N", "Sábado M/T", "Sábado T/N", "Domingo M/T", "Domingo T/N"]

dtanC.salvarJson(dataInicial, "data.json", "data")
jsonDiferencasAguaEnergia = dtanC.jsonDiferencasAguaEnergia(dataInicial)
dtanC.salvarJson(jsonDiferencasAguaEnergia, "diferencasAguaEnergia.json", "data")

dataDias = dtanC.carregarJson(r"data\diferencasAguaEnergia.json")
dataDias1 = dtanC.carregarJson(r"data\data.json")

dadosTabelaAgua = dtanC.modificarJsonAgua(dataDias1)
dadosTabelaEnergia = dtanC.modificarJsonEnergia(dataDias1)

diferencasDetalhadasAgua = dtanC.modificarJsonDiferencasAgua(dataDias)
diferencasDetalhadasEnergia = dtanC.modificarJsonDiferencasEnergia(dataDias)

diferencasTotalEnergia = dtanC.diferencasTotalEnergia(dataDias)
diferencasTotalAgua = dtanC.diferencasTotalAgua(dataDias)

maxEnergia, minEnergia = dtanC.maxMinEnergia(dataDias)
maxAgua, minAgua = dtanC.maxMinAgua(dataDias)
mediaAgua = dtanC.mediaAgua(dataDias)
mediaEnergia = dtanC.mediaEnergia(dataDias)

aguaManhaTarde, aguaTardeNoite, energiaManhaTarde, energiaTardeNoite = dtanC.periodosAguaEnergia(dataDias)

dtanG.tabelaDadosAgua(dadosTabelaAgua)
dtanG.tabelaDadosEnergia(dadosTabelaEnergia)
dtanG.graficoDiferencasAgua(diasSemanaDividos, diferencasDetalhadasAgua)
dtanG.graficoDiferencasEnergia(diasSemanaDividos, diferencasDetalhadasEnergia)
dtanG.graficoDiferencaTotal(diasSemana, diferencasTotalAgua, diferencasTotalEnergia)
dtanG.graficoPizza(aguaManhaTarde, aguaTardeNoite, energiaManhaTarde, energiaTardeNoite)
dtanG.dadosGerais(mediaAgua, mediaEnergia, maxEnergia, maxAgua, minEnergia, minAgua)
