from openpyxl.chart import (
    ScatterChart,
    Reference,
    Series,
)

# conta quantas colisoes aconteceram
def contar_ocorrencia(valores):
    quantidade = []
    dominio = set(valores)
    dominio = list(dominio)
    contador = 0
    for i in range(len(dominio)):
        for j in range(len(valores)):
            if dominio[i] == valores[j]:
                contador = contador + 1
        quantidade.append(contador)
        contador = 0

    return quantidade


# plota um grafico de linha no excel
def plotar_grafico(sheet, dominio):
    # desenhar grafico

    grafico = ScatterChart()
    grafico.title = "Valor Hash vs Numero de Colizões"
    grafico.style = 13
    grafico.x_axis.title = "Valores do Hash"
    grafico.y_axis.title = "N de colizoes"
    xvalue = Reference(sheet, min_col=1, min_row=2, max_row=len(dominio) + 1)
    values = Reference(sheet, min_col=2, min_row=1, max_row=len(dominio) + 1)
    series = Series(values, xvalue, title_from_data=True)
    grafico.series.append(series)
    sheet.add_chart(grafico, "E2")
