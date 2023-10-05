time = ["Palemiras",
        "Santos", "São Paulo",
        "Audax", "Corinthiams", "Leicester", "Derac"]
pontosGanhos = [34, 78, 34, 34, 56, 78, 78]
saldoGols = [-8, 67, 24, 47, 56, 45, 45]
golsMarcados = [12, 43, 43, 49, 36, 42, 41]
tamanho = int(7)


def ordenaPontosGanhos():
    replace = int(0)
    valida = bool(True)
    while (valida == True):
        valida = False
        for indicePontosGanhos in range(tamanho-1):
            if (pontosGanhos[indicePontosGanhos] < pontosGanhos[indicePontosGanhos+1]):
                replace = pontosGanhos[indicePontosGanhos]
                pontosGanhos[indicePontosGanhos] = pontosGanhos[indicePontosGanhos+1]
                pontosGanhos[indicePontosGanhos+1] = replace
                valida = True


def ordenaSaldoGols():
    replace = int(0)
    valida = bool(True)
    while (valida == True):
        valida = False
        for indiceSaldoGols in range(tamanho-1):
            if (saldoGols[indiceSaldoGols] < saldoGols[indiceSaldoGols+1]):
                replace = saldoGols[indiceSaldoGols]
                saldoGols[indiceSaldoGols] = saldoGols[indiceSaldoGols+1]
                saldoGols[indiceSaldoGols+1] = replace
                valida = True


ordenaPontosGanhos()
ordenaSaldoGols()


def displayResult():
    print("Classificação Ordenada")
    for x in range(0, tamanho):
        print(pontosGanhos[x], saldoGols[x])


displayResult()
