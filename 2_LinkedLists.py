# CTCI Questions & Answers
# CHAPTER 2: LINKEDLISTS

# My LinkedList Library
class Node:
  def __init__(self, value, n_next, n_prev):
    self.value = value
    self.n_next = n_next
    self.n_prev = n_prev

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head	# head and tail are the same at first
        self.ptr = self.head

    def insert(self, index, new_value):
        newNode = Node(new_value, None, None)
        #if empty, add as head:
        if self.head == None:
          self.head = newNode
          self.tail = newNode
          self.ptr = newNode
        #else, add into index
        else:
          #check if index exists:
          if index > self.get_size():
            return SyntaxError
          else:
            ptr = self.head
            prevNode = None
            count = 0
            #if inserting as new head:
            if count==index:
                existingNode = ptr
                newNode.n_next = existingNode
                self.head = newNode
                existingNode.n_prev = newNode
            else:
                #loop to the index
                while(count < index):
                  prevNode = ptr
                  ptr = ptr.n_next
                  count = count + 1
                existingNode = ptr
                prevNode.n_next = newNode
                newNode.n_prev = prevNode
                if existingNode:
                  newNode.n_next = existingNode
                  existingNode.n_prev = newNode
                else:
                    self.tail = newNode


    def print_linked_list(self):
        ptr = self.head
        print('[ ', end = '')
        while(ptr):
          print(ptr.value, end = ' ')
          ptr = ptr.n_next
        print(']')

    def get_size(self):
        size = 0
        ptr = self.head
        while(ptr):
          size = size + 1
          ptr = ptr.n_next
        return size

    def prev(self):
        if self.ptr.n_prev:
            self.ptr = self.ptr.n_prev
            return self.ptr.value

    def next(self):
        if self.ptr.n_next:
            self.ptr = self.ptr.n_next
            return self.ptr.value
        else:
            self.ptr = None
            return None

    def remove(self):
        #if current pointer exists
        if self.ptr:
            #if there is a next pointer
            if self.ptr.n_next:
                self.ptr.n_prev.n_next = self.ptr.n_next
                self.ptr.n_next.n_prev = self.ptr.n_prev
            else:
                #if this is the old tail
                self.prev()
                self.ptr.n_next = None
                self.tail = self.ptr
            return self


    def mergesort(self):
        size = self.get_size()
        if size <=1:
            return self
        else:
            #split lists - 1st list:
            first_list = self.ptr
            #split lists - get second list:
            middle_index = round(size/2)
            count = 0
            while count < middle_index:
                self.next()
                count = count + 1
            second_list = self.ptr

#helper for linkedlist creation
def populate_linkedlist(list):
    linkedlist = LinkedList()
    index = 0
    for number in list:
      linkedlist.insert(index, number)
      index = index + 1
    return linkedlist






#------------------------------------------------------------

# Q1: Remove Dups: Write code to remove duplicates from an unsorted LinkedLists. How to solve if a temporary buffer isn't allowed?

def question2_1_part1(linkedlist):
    print("----------\n" + "2.1 Remove Dups: Write code to remove duplicates from an unsorted LinkedList\n" + "Input : ", end='')
    linkedlist.print_linked_list()
    #initialize temporary buffer dictionary
    dict = {}
    #loop through the LinkedList
    while linkedlist.ptr:
        #check each value to see if it exists within dictionary
        if dict.get(linkedlist.ptr.value):
        #if value exists
            linkedlist.remove()
            if linkedlist.ptr != linkedlist.tail:
                linkedlist.next()
            else:
                return linkedlist
        else:
            dict[linkedlist.ptr.value] = linkedlist.ptr.value
            if linkedlist.ptr.n_next:
                linkedlist.next()
            else:
                print('Output: ', end = '')
                return linkedlist

def question2_1_part2(linkedlist):
    print("----------\n" + "2.1 Remove Dups: Write code to remove duplicates from an unsorted LinkedList WITHOUT BUFFER\n" + "Input : ", end='')
    linkedlist.print_linked_list()

    #loop through linkedlist:
    while linkedlist.ptr:
        currentNode = linkedlist.ptr
        while linkedlist.ptr.n_next:
            linkedlist.next()
            if linkedlist.ptr.value == currentNode.value:
                linkedlist.remove()
        linkedlist.ptr = currentNode
        if linkedlist.ptr.n_next:
            linkedlist.next()
        else:
            return linkedlist
    return linkedlist

# Q2: Implement an algo to find the kth to last element of a singly linked list
def question2_2(linkedlist, k):
    print("----------\n" + "2.2 Implement an algo to find the kth to last element of a singly linked list\n" + "Input: ", end='')
    linkedlist.print_linked_list()
    print('k = ', k)

    #find target index:
    size = linkedlist.get_size()
    index = size - k
    #check if kth index exists within linkedlist
    if index >= size:
        return SyntaxError
    else:
        #loop until target index
        count = 0
        while count < index:
            linkedlist.next()
            count = count + 1
        return linkedlist.ptr

# Q3: Implement an algo to delete a node in the middle of a singly linked list, given only access to that node.
def question2_3(node):
    print("----------\n" + "2.3 Implement an algo to delete a node in the middle of a singly linked list, given only access to that node.\n" + "Input: ", end='')
    print(node.value)
    #node is assumed not to be head or tail
    #replace node with next node, and so on.
    while(node.n_next):
        node.value = node.n_next.value
        node = node.n_next
        #the next node needs to be the last node, as there is a duplicate due to the sliding. That duplicate is cut off:
        if node.n_next.n_next == None:
            node.value = node.n_next.value
            node.n_next = None
            break


# Q4: Parition a linkedlist around a value X such that all nodes less than X come before nodes greater than X
def question2_4(linkedlist, x):
    print("----------\n" + "2.4 Parition a linkedlist around a value X such that all nodes less than X come before nodes greater than X\n" + "Input: ", end='')
    linkedlist.print_linked_list()

    first_half = LinkedList()
    second_half = LinkedList()
    while(linkedlist.ptr):
        if linkedlist.ptr.value < x:
            first_half.insert(first_half.get_size(), linkedlist.ptr.value)
        else:
            second_half.insert(second_half.get_size(), linkedlist.ptr.value)
        linkedlist.next()
    second_half.ptr = second_half.head
    while(second_half.ptr):
        first_half.insert(first_half.get_size(), second_half.ptr.value)
        second_half.next()
    return first_half

# Q5: Two numbers are represented by a linkedin. Add them in REVERSE ORDER
def question2_5_part1(a, b):
    print("----------\n" + "2.4 Parition a linkedlist around a value X such that all nodes less than X come before nodes greater than X. Digits stored in REVERSE ORDER.\n" + "Input: ", end='')
    a.print_linked_list()
    b.print_linked_list()
    numA = 0
    counter = 0
    while(a.ptr):
        numA = numA + a.ptr.value * 10**counter
        counter = counter + 1
        a.next()
    numB = 0
    counter = 0
    while(b.ptr):
        numB = numB + b.ptr.value * 10**counter
        counter = counter + 1
        b.next()
    return int(numA + numB)

# Q5.2: Two numbers are represented by a linkedin. Add them in FORWARD ORDER
def question2_5_part2(a, b):
    print("----------\n" + "2.5 Parition a linkedlist around a value X such that all nodes less than X come before nodes greater than X. Digits stored in FORWARD ORDER\n" + "Input: ", end='')
    a.print_linked_list()
    b.print_linked_list()
    numA = 0
    tensDigit = 10**(a.get_size()-1)
    while(a.ptr):
        numA = numA + a.ptr.value * tensDigit
        tensDigit = tensDigit/10
        a.next()
    numB = 0
    tensDigit = 10**(b.get_size()-1)
    while(b.ptr):
        numB = numB + b.ptr.value * tensDigit
        tensDigit = tensDigit/10
        b.next()
    return int(numA + numB)

#Check if a linkedlist is a palindrome
def question2_6(linkedlist):
    print("----------\n" + "2.6 Check if a linkedlist is a palindrome\n" + "Input: ", end='')
    linkedlist.print_linked_list()
    beginningPtr = linkedlist.ptr
    endPtr = linkedlist.tail
    middle_index = int(linkedlist.get_size()/2)
    counter = 0
    while(counter < middle_index):
        if beginningPtr.value != endPtr.value:
            return False
        counter = counter + 1
        beginningPtr = beginningPtr.n_next
        endPtr = endPtr.n_prev
    return True

# Given two singly linked lists, determine if they intersect. Return the intersecting node.
def question2_7(a, b):
    print("----------\n" + " Given two singly linked lists, determine if they intersect. Return the intersecting node.\n" + "Input: ")
    print('LinkedList 1: ', end='')
    a.print_linked_list()
    print('LinkedList 2: ', end='')
    b.print_linked_list()
    while(a.ptr):
        while(b.ptr):
            if a.ptr == b.ptr:
                return a.ptr
            b.next()
        a.next()
    return None

# Given a circular linkedlist, there is an earlier node that is the next node of an later node. return the node at the beginning of the loop.
def question2_8(circular):
    print("----------\n" + " Given a circular linkedlist, there is an earlier node that is the next node of an later node. return the node at the beginning of the loop.\n" + "Input: ", end='')
    #printing circular linkedlist -partially-
    counter = 6
    while (counter > 0):
        print(circular.ptr.value, end='')
        circular.next()
        counter = counter - 1
    circular.ptr = circular.head
    print()

    node_dict = {}
    #if node exists already
    while(circular.ptr.n_next):
        if node_dict.get(circular.ptr.n_next):
            return circular.ptr.n_next
        else:
            node_dict[circular.ptr.n_next] = 1
        circular.next()
    return None

#---------------------------------------------------------------
def main():
    print("LinkedList Python Library + Solutions to Chapter 2: LinkedLists")
    print("Written by Kamile Demir")
    #1
    question2_1_part1(populate_linkedlist([2,4,1,4,3,8,3])).print_linked_list()
    #1.2
    question2_1_part2(populate_linkedlist([2,4,1,4,3,8,3])).print_linked_list()
    #2
    print(question2_2(populate_linkedlist([2,4,1,4,5,8,3]),3).value)
    #3
    list = populate_linkedlist([2,4,1,9,5,8,3])
    count = 0
    node_index = 3
    while count < node_index:
        list.next()
        count = count + 1
    list.insert(0, 6)
    question2_3(list.ptr)
    print("LinkedList before: [2,4,1,9,5,8,3]")
    print("LinkedList after: ", end='')
    list.print_linked_list()
    #4
    question2_4(populate_linkedlist([2,4,1,4,5,8,3]), 4).print_linked_list()
    #5.1
    print(question2_5_part1(populate_linkedlist([7,1,6]), populate_linkedlist([5,9,2])))
    #5.2
    print(question2_5_part2(populate_linkedlist([6,1,7]), populate_linkedlist([2,9,5])))
    #6
    print(question2_6(populate_linkedlist([1,3,5,3,1])))
    print(question2_6(populate_linkedlist([1,3,3,1])))
    print(question2_6(populate_linkedlist([1,3,8,1])))
    #7
    a = populate_linkedlist([2,4,1,3])
    b = populate_linkedlist([1,7,5,4])
    intersection = Node(5,None,None)
    old = a.head
    a.head = intersection
    a.head.n_next = old.n_next
    old = b.head
    b.head = intersection
    b.head.n_next = old.n_next
    a.ptr = a.head
    b.ptr = b.head
    print(question2_7(a, b))
    #8
    #initialize circular LinkedList
    circular = populate_linkedlist(['A','B','C','D','E'])
    counter = 2
    while(counter > 0):
        circular.next()
        counter = counter - 1
    nodeC = circular.ptr
    counter = 2
    while(counter > 0):
        circular.next()
        counter = counter - 1
    nodeE = circular.ptr
    nodeE.n_next= nodeC
    circular.ptr = circular.head
    result = question2_8(circular)
    print('Node object:', result, 'Node value:', result.value)

main()
