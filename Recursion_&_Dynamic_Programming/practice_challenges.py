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

#you can perform the following operations on the string, :
# Capitalize zero or more of 's lowercase letters.
# Delete all of the remaining lowercase letters in .
# Given two strings,  and , determine if it's possible to make  equal to  as described. If so, print YES on a new line. Otherwise, print NO.

def abbreviation(a, b):
    lenA = len(a)
    lenB = len(b)
    if lenB>lenA: #b cannot be greater than A.
        print('14')
        return "NO"
    else:
        i = 0
        searching = False
        while i < lenA:
            if i >= lenB:
                # print('ever used?')
                ordB = ord(b[lenB-1])
            else:
                ordB = ord(b[i])
            ordA = ord(a[i])
            if ordA == ordB: #already equal & capital
                i = i + 1
                continue
            elif ordA - 32 == ordB: #needs capitalizing
                if i < lenA-1 and i < lenB-1 and ord(a[i+1]) == ordB and ordB != ord(b[i+1]):
                    a = a[0:i] + a[i+1:lenA]
                    lenA = lenA -1
                    # print("deleted?", a, b)
                    # i = i -1
                else:
                    a = a[0:i] + chr(ordB) + a[i+1:lenA]
                    i = i + 1
            else: #deleting
                if ordA < 91: #cannot delete uppercase
                    print(i, ordA, a[0:i+1])
                    return "NO"
                else: #deleting
                    a = a[0:i] + a[i+1:lenA]
                    lenA = lenA - 1
                if len(a) == len(b):
                    print(a, b)
                    print(lenA)
                    # i = i - 1
                    # if ord(a[i]) == ordB:
                    #     print(a[320:i+1])
                    #     print(i, ord(a[i]), ordB)
                    #     return "YES"
                if lenA < lenB:
                    print(i, a, b)
                    return "NO"
        # print(a, b)
        return "YES"
