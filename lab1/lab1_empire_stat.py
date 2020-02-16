import math
import numpy as np
import matplotlib.pyplot as plt
import lab1.my_array as mod
from statistics import median

array = mod.ret_array()
sorted_array = sorted(array)

def interval_variation_row(array):
        l = math.floor(1 + 3.32*math.log(len(array), 10)) # intervals quantity
        h = (np.amax(array) - np.amin(array)) / l # длина интервала групировки 12.875
        array_min = np.amin(array)

        interval_row = {}
        interval = []
        key = 1
        start = array_min
        stop = start + h
        for i in array:
                if start <= i < stop:
                        interval.append(i)
                elif i >= stop:
                        start = stop
                        stop += h
                        key += 1
                        interval = []
                        interval.append(i)

                interval_row[key] = sorted(interval)
        return interval_row, h


def group_sampling_frequency_table(row):
        funded_frequency = len(row[1])
        funded_relative = funded_frequency / 100
        print("                                           Relative    Funded      Funded")
        print(" N      Limits        Median   Frequency   frequency   frequency   relative" )
        for key in row:
                low = np.amin(row[key])
                high = np.amax(row[key])
                mediana = median(row[key])
                frequency = len(row[key])
                relative_frequency = frequency / 100
                if row[key] != row[1]:
                        funded_frequency += frequency
                        funded_relative += relative_frequency
                print(" %.0f    %.0f     %.0f       %.0f       %.0f        %.2f          %.0f        %.2f"
                      % (key, low, high, mediana, frequency, relative_frequency, funded_frequency, funded_relative))


def histogram_polygon(row):
        x = []
        y = []
        for key in row:
                x.append(np.amin(row[key]))
                y.append(len(row[key]) / 100)
        width = 12.875
        plt.bar(x, y, width, edgecolor='black')
        plt.plot(x, y, 'r--')

        plt.xticks(x)
        plt.show()


interval_row = interval_variation_row(sorted_array)
histogram_polygon(interval_row)
#  group_sampling_frequency_table(interval_row)
