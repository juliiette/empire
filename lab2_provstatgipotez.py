import lab1.my_array as mod
import math
import lab1.lab1_empire_stat as stat
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf

array = mod.ret_array()
array = sorted(array)

intervals = stat.count_intervals(array)
frequencies = stat.count_freq(array, intervals)
middles = stat.count_middles(intervals)
n = len(array)

Phi = lambda x: erf(x/2**0.5) / 2


def count_middles_sum(middles, frequencies, n):
    sum = 0
    x = 0
    for i in range(len(middles)):
        sum += (middles[i] ** 2) * frequencies[i]
        x += middles[i] * frequencies[i]
    sum = sum / n
    x = x / n
    Dx = sum - x ** 2
    rejection = math.sqrt(Dx)
    return x, rejection

def count_theory_frequencies(intervals, frequencies, x, rejection):
    zi = []
    zi_1 = []
    Fzi = []
    Fzi_1 = []
    ni_shtrih = []
    for i in range(len(frequencies)):
        zi.append(round(((min(intervals[i]) - x) / rejection) , 7))
        zi_1.append(round(((max(intervals[i]) - x) / rejection) , 7))

    for i in range(len(frequencies)):
        Fzi.append(round(Phi(zi[i]), 7))
        Fzi_1.append(round(Phi(zi_1[i]), 7))

    for i in range(len(frequencies)):
        ni_shtrih.append(round(200 * (Fzi_1[i] - Fzi[i]), 7))

    print("Intervals: ", intervals)
    print("Frequencies: ", frequencies)
    print("Zi:     ", zi, "\nZi+1:   ", zi_1)
    print("Ф(Zi):  ", Fzi, "\nФ(Zi+1): ", Fzi_1)
    print("n`i:  ", ni_shtrih)

    return ni_shtrih


def count_observation(ni_shtrih, frequencies):
    ni_npi = []
    ni_npi2 = []
    for i in range(len(frequencies)):
        value = frequencies[i] - ni_shtrih[i]
        ni_npi.append(round((value), 5))
        value = value ** 2
        ni_npi2.append(round((value), 5))

    x_obs = []
    freq_sqrt = []
    for i in range(len(frequencies)):
        x_obs.append(round((ni_npi2[i]/ni_shtrih[i]), 6))
        freq_sqrt.append(round((frequencies[i] ** 2), 6))
    x_observation = round(sum(x_obs), 6)

    division = []
    for i in range(len(frequencies)):
        division.append(round((freq_sqrt[i] / ni_shtrih[i]), 6))

    print("\nFrequencies:  ", frequencies)
    print("Ni`:   ", ni_shtrih)
    print("Ni*-NPi:  ", ni_npi, "\n(Ni*-NPi)^2:   ", ni_npi2)
    print("Xobsˆ2:  ", x_obs, "\nXobs = ", x_observation)
    print("Niˆ2/Ni:  ", division, "\nSum = ", round(sum(division), 6))

    return x_observation, sum(division)


def check_observation(x_observation, division_sum, n):
    x_obs = round(division_sum - n, 6)
    return x_obs


def critical_area(x_observation):
    X_critical = 15.1
    x = [0, 20.1]
    y = [0, 0]
    plt.plot(x, y)
    plt.scatter(X_critical, 0)
    plt.scatter(X_critical, 2)

    for i in range(11):
        plt.vlines(X_critical+i/2, 0, 0.1, color='r')

    plt.show()


if __name__ == "__main__":
    x, rejection = count_middles_sum(middles, frequencies, n)
    ni_shtrih = count_theory_frequencies(intervals, frequencies, x, rejection)
    x_observation, sum_division = count_observation(ni_shtrih, frequencies)
    print("\nCheck Xobs: ", check_observation(x_observation, sum_division, n))
    print("Xobs:       ", x_observation)

    critical_area(x_observation)
