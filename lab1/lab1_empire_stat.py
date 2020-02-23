import math
import numpy as np
import matplotlib.pyplot as plt
import lab1.my_array as mod
from statistics import median
import pandas as pd

array = mod.ret_array()
sorted_array = sorted(array)
l = math.floor(1 + 3.32 * math.log(len(array), 10))
h = (np.amax(array) - np.amin(array)) / l #  12.875
n = len(array)


def count_intervals(array):
        intervals = []
        stop = np.amin(array)
        for i in range(l):
                intervals.append([stop, stop+h])
                stop += h
        return intervals


def count_freq(array, intervals):
        frequencies = [0] * len(intervals)
        for i in range(len(intervals)):
                for item in array:
                        if i == 0 and intervals[i][0] <= item <= intervals[i][1]:
                                frequencies[i] += 1
                        if i != 0 and intervals[i][0] < item <= intervals[i][1]:
                                frequencies[i] += 1
        return frequencies


def funded_relative_freq_arr(row):              # 4 zadanie dlya histogrami
        funded_relative = len(row[1]) / 100
        funded_relative_arr = [funded_relative]
        for key in row:
                frequency = len(row[key])
                relative_frequency = frequency / 100
                if row[key] != row[1]:
                        funded_relative += relative_frequency
                        funded_relative_arr.append(funded_relative)
        return funded_relative_arr


def group_sampling_frequency_table(array, intervals, frequencies):
        medians = []
        funded_freq = 0
        funded_freq_arr = []
        relative_freq_arr = []
        funded_relative = 0
        funded_relative_arr = []
        for key in range(len(intervals)):
                medians.append(median(intervals[key]))
                funded_freq = funded_freq + frequencies[key]
                funded_freq_arr.append(funded_freq)
                relative_freq_arr.append(frequencies[key] / len(array))
                funded_relative = funded_relative + (frequencies[key] / len(array))
                funded_relative_arr.append(funded_relative)
        return medians, funded_freq_arr, relative_freq_arr, funded_relative_arr


def print_table():
        print("Frequency Table:")
        print("Limits: ", intervals)
        print("Interval Middle: ", medians)
        print("Frequency: ", freq)
        print("Funded Frequencies: ", funded_freq)
        print("Relative Frequencies: ", rel_freq)
        print("Funded Frequencies: ", funded_rel)


def medians_frequency_histogram():
        x = medians
        y = rel_freq
        width = h
        plt.bar(x, y, width, edgecolor='black', color='white')
        plt.plot(x, y, 'b--')
        plt.xticks(x)
        plt.show()


def medians_funded_relative_histogram():
    x = medians
    y = funded_rel
    width = h
    plt.bar(x, y, width, edgecolor='black', color='white')
    plt.plot(x, y, 'b--')
    plt.xticks(x)
    plt.show()


def empire_spreading_func(intervals, funded_relative):
    y = []
    for i in range(len(funded_relative)):
        y.append([funded_relative[i], funded_relative[i]])

    for i in range(len(intervals)):
        plt.plot(intervals[i], y[i])
    plt.grid(True)
    plt.show()


global interval_number
def moda_func():
        max_freq = np.amax(freq)
        key = freq.index(max_freq)

        interval_number = 0
        for i in range(len(freq)):
                if (freq[i] > freq[interval_number]):
                        interval_number = i
        min_interval_value = intervals[interval_number][0]
        freq_interval = freq[interval_number]
        if (interval_number == 0):
                freq_before_interv = 0
        else:
                freq_before_interv = freq[interval_number - 1]
        if (interval_number == 7):
                freq_after_interv = 0
        else:
                freq_after_interv = freq[interval_number + 1]
        return min_interval_value + h * (
                        (freq_interval - freq_before_interv) / (2 * freq_interval - freq_before_interv - freq_after_interv))


def median_func(intervals):
    global interval_number
    for i in range (len(intervals)):
        if(funded_freq[i] > 100) :
            interval_number = i+1
            break
    minIntervValue = intervals[interval_number-1][0]
    freqInterv = freq[interval_number-1]
    accumFreqBeforeInterval = funded_freq[interval_number - 2]
    print("Median")
    print("Interval Number - ",  interval_number)
    print("Minimal interval value - ", minIntervValue)
    print("Interval frequency - ", freqInterv)
    print("Accumulated frequency before interval - ", accumFreqBeforeInterval)
    return minIntervValue + h*((100 - accumFreqBeforeInterval)/(freqInterv))


def interval_stat_row():
    print("Intervals:", intervals)
    print("Frequencies:   ", freq)


def count_middles(intervals):
    middles = []
    for i in intervals:
        middle = ((min(i) + max(i))/2)
        middles.append(middle)
    return middles


def conditional_options(frequencies, middles):
    index = frequencies.index(np.amax(frequencies))
    zero = middles[index]
    uk = []
    for i in range(len(frequencies)):
        uk.append((middles[i]-zero)/h)

    uknk = [uk[i] * frequencies[i] for i in range(len(uk))]
    uk2 = [uk[i] ** 2 for i in range(len(uk))]
    uk2nk = [uk2[i] * frequencies[i] for i in range(len(uk))]
    print("dx = ", zero)
    print("nk:    ", middles, "\nuk:    ", uk, "\nuknk:  ", uknk, "\nuk^2:  ", uk2, "\nuk^2nk:", uk2nk)

    u = (1/n)*sum(uknk)
    Du = (1/n)*sum(uk2nk)-u**2
    x = h * u + zero
    Dx = h**2 * Du
    rejection = math.sqrt(Dx)
    return x, Dx, rejection, zero


def central_moments(middles, x, frequencies, k):
    moment = 0
    for i in range(len(frequencies)):
        moment += ((middles[i]-x)**k)*frequencies[i]
    return moment/n


def asymmetry_coef(moment3, rejection):
    As = moment3 / (rejection**3)
    return As


def excess_coef(moment4, rejection):
    Es = moment4 / (rejection**4) - 3
    return Es


def stat_estimation(x, Dx, t):
    interval = [0, 0]
    rejection = math.sqrt((n * Dx)/(n-1))
    interval[0] = x - t * rejection/math.sqrt(n)
    interval[1] = x + t * rejection/math.sqrt(n)
    return interval


intervals = count_intervals(sorted_array)
freq = count_freq(sorted_array, intervals)
medians, funded_freq, rel_freq, funded_rel = group_sampling_frequency_table(sorted_array, intervals, freq)
middles = count_middles(intervals)
x, Dx, rejection, zero = conditional_options(freq, middles)
moment3 = central_moments(middles, x, freq, 3)
moment4 = central_moments(middles, x, freq, 4)
dov_interv = stat_estimation(x, Dx, 2.627)
print("\nRejection = ", math.sqrt((n * Dx)/n-1), "\nt = ", 2.627)
print(dov_interv[0], " < X < ", dov_interv[1])


#print("\nx = ", x, "\nDx = ", Dx, "\nrejection = ", rejection)
#print("\nSelective central moment 3: ", moment3, "\nAsymmetry: ", asymmetry_coef(moment3, rejection))
#print("\nSelective central moment 4: ", moment4, "\nExcess: ", excess_coef(moment4, rejection))
