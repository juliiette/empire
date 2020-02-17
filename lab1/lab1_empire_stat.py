import math
import numpy as np
import matplotlib.pyplot as plt
import lab1.my_array as mod
from statistics import median
import pandas as pd

array = mod.ret_array()
sorted_array = sorted(array)
l = math.floor(1 + 3.32 * math.log(len(array), 10))
h = (np.amax(array) - np.amin(array)) / l


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


def print_table(intervals):
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
        width = 12.875
        plt.bar(x, y, width, edgecolor='black', color='white')
        plt.plot(x, y, 'r--')
        plt.xticks(x)
        plt.show()


def medians_funded_relative_histogram():
    x = medians
    y = funded_rel
    width = 12.875
    plt.bar(x, y, width, edgecolor='black', color='white')
    plt.plot(x, y, 'r--')
    plt.xticks(x)
    plt.show()


global interval_number
def moda_func():
        max_freq = np.amax(freq)
        key = freq.index(max_freq)

        interval_number = 0
        for i in range(len(freq)):
                if (freq[i] > freq[interval_number]):
                        interval_number = i
        print("Interval num:            ", interval_number + 1)
        min_interval_value = intervals[interval_number][0]
        print("Minimal value:           ", min_interval_value)
        freq_interval = freq[interval_number]
        print("Interval frequency:      ", freq_interval)
        if (interval_number == 0):
                freq_before_interv = 0
        else:
                freq_before_interv = freq[interval_number - 1]
        print("Before modal frequency:  ", freq_before_interv)
        if (interval_number == 7):
                freq_after_interv = 0
        else:
                freq_after_interv = freq[interval_number + 1]
        print("After modal frequency:   ", freq_after_interv)
        return min_interval_value + h * (
                        (freq_interval - freq_before_interv) / (2 * freq_interval - freq_before_interv - freq_after_interv))


def median_func():
    global interval_number
    for i in range (8):
        if(funded_freq[i] > 100) :
            interval_number = i
            break
    print("Interval Number:                  ", interval_number + 1)
    minIntervValue = intervals[interval_number][0]
    print("Minimal interval value:           ", minIntervValue)

    freqInterv = freq[interval_number]
    print("Interval frequency:               ", freqInterv)
    accumFreqBeforeInterval = funded_freq[interval_number - 1]
    print("Funded frequency before interval: ", accumFreqBeforeInterval)
    return minIntervValue + h*((100 - accumFreqBeforeInterval)/(freqInterv))


intervals = count_intervals(sorted_array)
freq = count_freq(sorted_array, intervals)
medians, funded_freq, rel_freq, funded_rel = group_sampling_frequency_table(sorted_array, intervals, freq)
moda = moda_func()
mediana = median_func()

