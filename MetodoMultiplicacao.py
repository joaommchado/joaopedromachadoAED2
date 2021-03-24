import math
def inserir_valor(dominio, quantidade):
    pass
def contar_ocorrencia(valores):
    quantidade = []
    dominio = set(valores)
    dominio = list(dominio)
    print(dominio)
    contador = 0
    for i in range(len(dominio)):
        for j in range(len(valores)):
            if(dominio[i] == valores[j]):
                contador = contador + 1
        quantidade.append(contador)
        contador = 0

    #inserir_valores(dominio, quantidade)

def espalhamento_multi():
    # planilha = Workbook()
    # planilha = planilha.active

    key = int(input())
    m = int(input())
    a = float(input())

    h = list()
    for i in range(key):
        h.append(int(math.floor(m * ((i * a) % 1))))

    contar_ocorrencia(h)


if __name__ == '__main__':
    espalhamento_multi()
