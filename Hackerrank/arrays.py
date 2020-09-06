#!/bin/python3

import math
import os
import random
import re
import sys

# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates.
# You are allowed to swap any two elements.
# You need to find the minimum number of swaps required to sort the array in ascending order.



def minimumSwaps(arr):
    index = 0 #current index
    value = 1 #value 1 -> N 
    count = 0 #count of swaps
    while index < len(arr): #traverse array until the end
        if arr[index] != value: #if current index does not hold the value it should (there exist values 1...N in this array)
            current = arr[index] #recording current value at current index
            new = arr[current-1] #recording new value at index currentValue
            arr[current-1] = arr[index] #swap: current value goes to its rightful index
            arr[index] = new #swap: old value at that index swapped for current index
            count = count + 1 #increment counter
        else: #keep traversing
            index = index + 1
            value = value + 1
    return count
