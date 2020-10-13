# HACKERRANK: Max Array Sum
# Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.
def maxSubsetSum(arr):
    m = [None]*len(arr)
    m[0]= arr[0]
    m[1] = max(arr[1], m[0])
    i = 2
    while i < len(arr):
        m[i] = max(arr[i], arr[i] + m[i-2], m[i-1])
        i = i + 1
    return m[i-1]
