from openpyxl import Workbook
from Colisoes import contar_ocorrencia, plotar_grafico
from openpyxl.styles import Font


# Coloca os valores na planilha e destaca os valores de hash igual a 3
def preencher_planilha(sheet, key, m):
    dominio = []
    # Definindo cabecalho
    sheet["A1"] = "Valor K (Key)"
    sheet["B1"] = "Valor M (Modulo)"
    sheet["C1"] = "Valor H(X)"

    sheet["A1"].font = Font(color='FF0000', bold=True)
    sheet["B1"].font = Font(color="FF0000", bold=True)
    sheet["C1"].font = Font(color="FF0000", bold=True)

    for i in range(1, key + 1):
        celula1 = "A"
        celula2 = "B"
        celula3 = "C"

        valor1 = celula1 + str(i + 2)
        valor2 = celula2 + str(i + 2)
        valor3 = celula3 + str(i + 2)

        sheet[valor1] = i
        sheet[valor2] = m
        sheet[valor3] = i % m
        dominio.append(i % m)

        if sheet[valor3].value == 3:
            sheet[valor1].font = Font(color='009999FF', bold=True)
            sheet[valor2].font = Font(color='009999FF', bold=True)
            sheet[valor3].font = Font(color='009999FF', bold=True)

    return dominio


# Adiciona os valores na planilha da colisao
def inserir_valores_colisoes(sheet, dominio, quantidade):
    celula1 = "A"
    celula2 = "B"

    sheet["A1"] = "Valor K (Key)"
    sheet["B1"] = "Numero de colisoes"
    sheet["A1"].font = Font(color='FF0000', bold=True)
    sheet["B1"].font = Font(color="FF0000", bold=True)

    for i in range(len(dominio)):
        valor1 = celula1 + str(i + 2)
        valor2 = celula2 + str(i + 2)

        sheet[valor1] = dominio[i]
        sheet[valor2] = quantidade[i]
        plotar_grafico(sheet, dominio)


# inicia o codigo, pode ser importada para outros casos
def espalhamento_div():
    planilha = Workbook()
    valores_iniciais = planilha.create_sheet("Valores", 0)
    colizoes = planilha.create_sheet("Valores", 1)

    k = int(input())
    if k <= 0:
        raise Exception("K deve ser maior que zero")
    m = int(input())
    if m <= 0:
        raise Exception("M deve ser maior que zero")

    dominio = preencher_planilha(valores_iniciais, k, m)
    quantidade = contar_ocorrencia(dominio)
    dominio = set(dominio)
    dominio = list(dominio)
    inserir_valores_colisoes(colizoes, dominio, quantidade)

    planilha.save(filename="1a.xls")


if __name__ == '__main__':
    espalhamento_div()
