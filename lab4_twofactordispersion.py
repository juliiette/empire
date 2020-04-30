# сразу стоит извиниться перед теми, кто это увидит - мне было слишком лень писать красиво
# и я написала с минимальными усилиями, просто чтобы оно работало
# надеюсь, ваши глаза не будут кровоточить

import numpy as np

array = [[1, 2, 2, 3, 6],
         [8, 5, 5, 7, 3],
         [3, 9, 4, 3, 9],
         [5, 4, 4, 6, 8],
         [4, 5, 2, 9, 6],
         [4, 2, 1, 5, 3]]


def summirizeFactor(array):
    E = []
    EA = []
    EB = []
    for row in array:
        E.append(np.sum(row))

    i = 0
    while i < 6:
        EA.append(E[i] + E[i+1])
        i += 2

    EB.append(E[0] + E[2] + E[4])
    EB.append(E[1] + E[3] + E[5])
    return E, EA, EB


E, EA, EB = summirizeFactor(array)
n = len(array[0])
a = len(EA)
b = len(EB)


def calculateRowSum(E, EA, EB):
    ET2A = 0
    ET2B = 0
    ET2AB = 0
    i = 0
    while i < len(EA):
        ET2A += EA[i] ** 2
        i += 1

    i = 0
    while i < len(EB):
        ET2B += EB[i] ** 2
        i += 1

    i = 0
    while i < len(E):
        ET2AB += E[i] ** 2
        i += 1
    return ET2A, ET2B, ET2AB


def calculateOtherParameters(array):
    n = len(array[0])
    Exi = np.sum(array)
    Exi2 = Exi ** 2
    C = Exi2 / 30
    Ex2i = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            Ex2i += array[i][j] ** 2
    return Exi, Exi2, C, Ex2i

ET2A, ET2B, ET2AB = calculateRowSum(E,EA, EB)
Exi, Exi2, C, Ex2i = calculateOtherParameters(array)

SSa = round(ET2A / (n * b) - C, 2)
SSb = round(ET2B / (n * a) - C, 2)
SSab = round(ET2AB / n - C - SSa - SSb, 2)
SSzag = round(Ex2i - C, 2)
SSvip = round(SSzag - SSa - SSb - SSab, 2)

dfA = a - 1
dfB = b - 1
dfAB = dfA * dfB
dfzag = 30 - 1
dfvip = dfzag - dfA - dfB - dfAB

MSa = round(SSa / dfA, 2)
MSb = round(SSb / dfB, 2)
MSab = round(SSab / dfAB, 2)
MSvip = round(SSvip / dfvip, 2)

Fa = round(MSa / MSvip, 2)
Fb = round(MSb / MSvip, 2)
Fab = round(MSab / MSvip, 2)


print("Сума по підрівню: ", E, "\nСума по А: ", EA, "\nСума по B: ", EB)
print("\nE(Ta)ˆ2: ", ET2A, "\nE(Tb)ˆ2: ", ET2B, "\nE(Tab)ˆ2: ", ET2AB)
print("n: ", n, "\na: ", a, "    b: ", b, "\nN: ", 30)
print("Exi: ", Exi, "\n(Exi)ˆ2: ", Exi2, "\nC: ", C, "\nExiˆ2: ", Ex2i)
print("\nSSa: ", SSa, "\nSSb: ", SSb, "\nSSab: ", SSab, "\nSSзаг: ", SSzag, "\nSSвип: ", SSvip)
print("dfA: ", dfA, "\ndfB: ", dfB, "\ndfAB: ", dfAB, "\ndfзаг: ", dfzag, "\ndfвип: ", dfvip)
print("MSa: ", MSa, "\nMSb: ", MSb, "\nMSab: ", MSab, "\nMSвип: ", MSvip)
print("Fa: ", Fa, "\nFb: ", Fb, "\nFab: ", Fab)

