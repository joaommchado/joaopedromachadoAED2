import math
from Colisoes import contar_ocorrencia, plotar_grafico
from openpyxl import Workbook
from openpyxl.styles import Font


# insere os valores na planilha
def inserir_valores(dominio, quantidade):
    planilha = Workbook()
    sheet = planilha.active
    sheet["A1"] = "Valores do Hash"
    sheet["B1"] = "Numero de colisoes"

    celula1 = "A"
    celula2 = "B"
    sheet["A1"].font = Font(color='FF0000', bold=True)
    sheet["B1"].font = Font(color="FF0000", bold=True)

    for i in range(len(dominio)):
        valor1 = celula1 + str(i + 2)
        valor2 = celula2 + str(i + 2)

        sheet[valor1] = dominio[i]
        sheet[valor2] = quantidade[i]

    plotar_grafico(sheet, dominio)
    planilha.save(filename="2_b.xls")


# realiza o tratamento das colisoes
def colisoes(valores):
    dominio = set(valores)
    quantidade = contar_ocorrencia(valores)
    dominio = list(dominio)
    inserir_valores(dominio, quantidade)


# inicia o codigo, pode ser importada para outros casos
def espalhamento_multi():
    key = int(input())
    if key <= 0:
        raise Exception("K deve ser maior que zero")
    m = int(input())
    if m <= 0:
        raise Exception("M deve ser maior que zero")
    a = float(input())
    if a > 1 or a < 0:
        raise Exception("A deve estar entre: [0,1]")

    h = list()
    for i in range(key):
        h.append(int(math.floor(m * ((i * a) % 1))))

    colisoes(h)


if __name__ == '__main__':
    espalhamento_multi()
