import data_analysis.calculos as dtanC
import data_analysis.graficos as dtanG

diasSemana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

dataDias = dtanC.carregarJson("data/diferencasAguaEnergia.json")

diferencasTotalEnergia = dtanC.diferencasTotalEnergia(dataDias)
diferencasTotalAgua = dtanC.diferencasTotalAgua(dataDias)

maxEnergia, minEnergia = dtanC.maxMinEnergia(dataDias)
maxAgua, minAgua = dtanC.maxMinAgua(dataDias)
mediaAgua = dtanC.mediaAgua(dataDias)
mediaEnergia = dtanC.mediaEnergia(dataDias)

dtanG.graficoDiferencaTotal(diasSemana, diferencasTotalAgua, diferencasTotalEnergia)
dtanG.dadosGerais(mediaAgua, mediaEnergia, maxEnergia, maxAgua, minEnergia, minAgua)
