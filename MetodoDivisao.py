from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.chart import (
    BarChart,
    Reference,
)

def inserir_valores(sheet, i, m):
    celula1 = "A"
    celula2 = "B"
    celula3 = "C"

    valor1 = celula1 + str(i + 2)
    valor2 = celula2 + str(i + 2)
    valor3 = celula3 + str(i + 2)

    sheet[valor1] = i
    sheet[valor2] = m
    sheet[valor3] = i % m

    if sheet[valor3].value == 3:
        sheet[valor1].font = Font(color='009999FF', bold=True)
        sheet[valor2].font = Font(color='009999FF', bold=True)
        sheet[valor3].font = Font(color='009999FF', bold=True)

    return i % m


def preencher_planilha(sheet, key, m):
    # Definindo cabecalho
    sheet["A1"] = "Valor K (Key)"
    sheet["B1"] = "Valor M (Modulo)"
    sheet["C1"] = "Valor H(X)"

    sheet["A1"].font = Font(color='FF0000', bold=True)
    sheet["B1"].font = Font(color="FF0000", bold=True)
    sheet["C1"].font = Font(color="FF0000", bold=True)

    for i in range(1, key + 1):
        inserir_valores(sheet, i, m)
        #colisoes[valor] = colisoes[valor] + 1
        #colisoes = colisoes[0:97]
        #return colisoes


def definir_colisoes(sheet, colisoes, key):
    celula1 = "A"
    celula2 = "B"

    sheet["A1"] = "Valor K (Key)"
    sheet["B1"] = "Numero de colisoes"
    sheet["A1"].font = Font(color='FF0000', bold=True)
    sheet["B1"].font = Font(color="FF0000", bold=True)

    for i in range(97):

        valor1 = celula1 + str(i + 2)
        valor2 = celula2 + str(i + 2)

        sheet[valor1] = i
        sheet[valor2] = colisoes[i]

    # desenhar grafico

    grafico = BarChart()
    sheet.add_chart(grafico, "A15")
    grafico.title = "Valor Hash vs Numero de Colizões"
    grafico.style = 13
    grafico.x_axis.title = "Valores do Hash"
    grafico.y_axis.title = "N de colizoes"
    data = Reference(sheet, min_col = 1, min_row = 2, max_col=2, max_row = key)
    grafico.add_data(data, from_rows = 2, titles_from_data = True)



def espalhamento_div():
    planilha = Workbook()
    sheet = planilha.active

    k = int(input())
    m = int(input())

    preencher_planilha(sheet, k, m)

    planilha.save(filename="projetoAed1.xls")


if __name__ == '__main__':
    espalhamento_div()
