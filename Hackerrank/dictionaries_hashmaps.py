import math
import os
import random
import re
import sys


def checkMagazine(magazine, note):
    mag_dict = {}
    for word in magazine:
        if word not in mag_dict:
            mag_dict[word] = 1
        else:
            mag_dict[word] = mag_dict[word] + 1

    for word in note:
        if word not in mag_dict:
            print('No')
            return
        else:
            if mag_dict[word] < 1:
                print('No')
                return
            else:
                mag_dict[word] = mag_dict[word]-1
    print('Yes')


def sherlockAndAnagrams(s):
    lists={}
    i = 0
    count = 0
    while i<len(s):
        j = 0
        while j <= i:
            substring = s[j:i+1]
            substring = ''.join(sorted(substring))
            print(substring)
            if substring in lists:
                count+=lists[substring]
                lists[substring] = lists[substring] + 1
            else:
                lists[substring] = 1
            j = j + 1
        i = i + 1
    print(lists)
    return count
