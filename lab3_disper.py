import numpy as np
import statistics
from scipy.stats import f

array = [[5, 8, 6, 9, 6],
         [6, 5, 8, 7, 8],
         [3, 6, 7, 7, 7]]


quant = []
sum = []
average = []
dispersion = []
standard_devitation = []

for row in array:
    quant.append(len(row))
    sum.append(np.sum(row))
    average.append(np.average(row))
    dispersion.append(round(statistics.variance(row), 1))
    standard_devitation.append(round(statistics.stdev(row), 7))

full_average = np.average(array)

def simple_table():
    print("Кількість: ", quant, "\nСума: ", sum, "\nСереднє: ", average, "\nДисперсія: ", dispersion, "\nСтанд. відхилення: ", standard_devitation)


selection_quantity = len(array)
elem_quantity = 0
for row in array:
    elem_quantity += len(row)
k1 = elem_quantity - selection_quantity
k2 = selection_quantity - 1
a = 0.5
F = 3.6823


def diff_table():
    print("Всього ел.: ", elem_quantity, "\nК-ть вибірок: ", selection_quantity, "\nk1: ", k1, "\nk2: ", k2, "\na: ", a, "\nF", F)


def evaluate_stat_dispersion(array, average):
    evaluation = []
    for i in range(len(array)):
        evaluation.append([])
        for j in range(len(array[i])):
            evaluation[i].append(round(((array[i][j] - average[i])**2), 6))

    for row in evaluation:
        print(row)
        
    return evaluation

eval = evaluate_stat_dispersion(array, average)

def table_dispersion(array, quant, average, full_average, eval, k2, k1):
        outgroup_dispersion = []
        for i in range(len(array)):
            outgroup_dispersion.append(round((5*(average[i]-full_average)**2), 6))
        sum = np.sum(outgroup_dispersion)
        ingroup_dispersion = np.sum(eval)
        full_dispersion = round(ingroup_dispersion + sum, 5)
        F = round((sum/k2)/(ingroup_dispersion/k1), 5)
        P = round(f.cdf(F, k1, k2), 5)

        print("Міжгр. дисперсія: ", outgroup_dispersion, "\nСума: ", sum, "\nВнутр. дисперсія: ", ingroup_dispersion)
        print("Заг. дисперсія: ", full_dispersion, "\nF: ", F, "\nP: ", P)


table_dispersion(array, quant, average, full_average, eval, k2, k1)
