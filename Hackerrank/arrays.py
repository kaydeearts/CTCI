#!/bin/python3

import math
import os
import random
import re
import sys


# There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue.
# Initial positions increment by  from  at the front of the line to  at the back.
# Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line.
# Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!
def minimumBribes(q):
    count = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i]-2),i):
            if q[j] > q[i]:
                count+=1
    print(count)

# Lilah has a string, , of lowercase English letters that she repeated infinitely many times.
# Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string
# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    for i in s:
        if i == 'a':
            count = count + 1
    leftover = n % len(s)
    full_sets = n - leftover
    count = count * (full_sets / len(s))
    index = 0
    while leftover > 0:
        if s[index] == 'a':
            count = count + 1
        index = index + 1
        leftover = leftover - 1
    return int(count)

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


# Complete the arrayManipulation function below.
# Starting with a 1-indexed array of zeros and a list of operations,
# for each operation add a value to each of the array element between two given indices, inclusive.
# Once all operations have been performed, return the maximum value in your array.
def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    for update in queries:
        arr[update[0]-1] = arr[update[0]-1] + update[2]
        arr[update[1]] = arr[update[1]] + (-1 * update[2])
    adding = 0
    index = 0
    maxNum = 0
    while index < n:
        # arr[index] = arr[index] + adding
        if arr[index] != 0:
            adding = arr[index] + adding
        if adding > maxNum:
            maxNum = adding
        index = index + 1
    return maxNum
