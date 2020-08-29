# CTCI Questions & Answers
# CHAPTER 1: ARRAYS & STRINGS

#Q1.1: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?


def question1_1(string):
    print("----------\n" + "1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?\n" + "Input: " + string)
    for a in string:
        for b in string:
            if a == b:
                return "Output: Not Equal"
    return "Output: Equal"

#Q1.2: Given two strings, write a method to decide if one is a permutation of the other.

def question1_2(string1, string2):
    print("----------\n" + "1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.\n" + "Input: " + string1 + " and " + string2)
    string1_len = len(string1)
    hashtable = ["False"] * 57
    counter = 0
    for a in string1:
        hashtable.insert(ord(a)-65, "True")
        counter = counter + 1
    counter = 0
    for b in string2:
        if hashtable[ord(b)-65] != "True":
            return "Output: False"
    return "Output: Valid permutations"

#Q1.3: Write a method to replace all spaces in a string with '%20'.

def question1_3(string):
    print("----------\n" + "1.3 URLify: Write a method to replace all spaces in a string with '%20'.\n" + "Input: " + string)
    newString = ""
    for char in string:
        if ord(char) == 32:
            newString = newString + "%20"
        else:
            newString = newString + char
    return "Output: " + newString

#Q4: Palindrome Permutation
def question1_4(string):
    print("----------\n" + "1.4 Palindrome Permutation: Check if a string is a permutation of a palindrome. \n" + "Input: " + string)
    # make every letter lowercase
    if string.isupper():
        string = string.lower()
    string = string.replace(" ", "")
    # hashtable to record amount per letter
    hashtable = [0] * 30
    # populate hashtable with string letters
    for char in string:
        index = ord(char) - 97
        number = hashtable[index] + 1
        hashtable[index] = number
    # check if more than one indexes appear only once. If so, this is not a valid permutation of a palindrome.
    counter = 0
    i = 0
    while i != len(hashtable):
        if hashtable[i] == 1:
            # print(i)
            counter = counter + 1
        i = i + 1
    if counter > 1:
        return "Output: False; not a valid palindrome"
    else:
        return "Output: True; valid palindrome"

# Q5: One Away: Write a function to determine if a two strings are one/zero edits away.
def question1_5(string1, string2):
    print("----------\n" + "1.5 One Away: Write a function to determine if a two strings are one/zero edits away. \n" + "Input: " + string1 + ", " + string2)
    # @var diffLengths: are lengths same or different?
    diffLengths = False
    len1 = len(string1)
    len2 = len(string2)
    if len1 != len2:
        diffLengths = True
    # if first string larger than second string, switch for implementation purposes.
    if len1 > len2:
        temp = string2
        string2 = string1
        string1 = temp
    # @var counter: count differences between the strings
    counter = 0
    # @var i: index for smaller string to insert space into when needed
    i = 0;
    # iterate through both strings to compare
    while i < len(string2):
        if string1[i] != string2[i]:
            counter = counter + 1
            if counter > 1:
                return "Output: Not valid, more than 1 edits away"
            if diffLengths:
                string1 = string1[:i] + "_" + string1[i:]
                diffLengths = False
        i = i + 1
    return "Output: " + str(counter) +" edits away"

# Q6: String Compression: Implement basic compression using counts of repeated characters
def question1_6(string):
    print("----------\n" + "1.6 String Compression: Implement basic compression using counts of repeated characters. \n" + "Input: " + string)
    # @var currChar: current char to compress
    currChar = string[0]
    currCount = 0
    newString = ""
    # adding "_" to end of string to indicate end of string (to keep from repetitive code)
    string = string + "_"
    for char in string:
        if char != currChar:
            newString = newString + currChar + str(currCount)
            currChar = char
            currCount = 1
        else:
            currCount = currCount + 1
    return newString

# Q7: Rotate Matrix: Given an image represented by an NxN matrix, where each pixel is 4 bytes, write a method to rotate the image by 90 degrees.
def question1_7(matrix):
    print("----------\n" + "1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel is 4 bytes, write a method to rotate the image by 90 degrees in place. \n" + "Input: " + str(matrix))
    # NxN dimensions of matrix:
    N = len(matrix)
    string = ""
    # place all matrix items within string
    a = 0
    b = 0
    while a < N:
        while b < N:
            string = string + matrix[a][b]
            b = b + 1
        b = 0
        a = a + 1
    begIndex = N*N - 3
    index = begIndex
    counter = 0
    i = 0
    j = 0
    while counter != N*N:
        # current row, next column:
        matrix[i][j] = string[index]
        if j != N-1:
            j = j + 1
            index = index - 3
        # new row:
        else:
            i = i + 1
            j = 0
            begIndex = begIndex + 1
            index = begIndex
        counter = counter + 1
    print("Output:")
    for a in matrix:
        print(a)

# Q8: Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0
def question1_8(matrix):
    print("----------\n" + "1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0 \n" + "Input: " + str(matrix))
    # get MxN dimensions
    M = len(matrix)
    N = len(matrix[0])
    a = 0
    b = 0
    list = []
    while a < M:
        while b < N:
            if matrix[a][b] == 0:
                list.append(a)
                list.append(b)
            b = b + 1
        a = a + 1
    helper1_8(list, matrix, N, M)
    print("Output:")
    for a in matrix:
        print(a)

def helper1_8(list, matrix, N, M):
    list_length = len(list)
    listCounter = 0
    while(listCounter < list_length):
        a = list[listCounter]
        b = list[listCounter+1]
        listCounter = listCounter + 2
        row = 0
        col = 0
        counter = 0
        # changing rows
        while(col < N):
            matrix[a][col] = 0
            col = col + 1
            counter = 0
            while(row < M):
                matrix[row][b] = 0
                row = row + 1
                counter = counter + 1

def question1_9(string1, string2):
    print("----------\n" + "1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another. Check if String2 is a rotation of String1 using one call to isSubstring \n" + "Input: " + string1 + ", " + string2)
    newString = string2 + string2
    # "in" is isSubstring within Python:
    if string1 in newString:
        return "True: " + string2 + " is a rotation of " + string1
    else:
        return "False: " + string2 + " is NOT a rotation of " + string1

def main():
    print("Solutions to Chapter 1: Arrays and Strings")
    print("Written by Kamile Demir")
    print(question1_1("ab"))
    print(question1_2("ab", "bac"))
    print(question1_3("This is pretty easy"))
    print(question1_4("booger"))
    print(question1_5("ble", "blue"))
    print(question1_6("aabcccccaaa"))
    question1_7_input = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    print(question1_7(question1_7_input))
    question1_8([[0,1,2,3], [3,4,5,6], [6,7,8,9]])
    print(question1_9("waterbottle", "erbottlewat"))

main()
