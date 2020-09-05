# CTCI Questions & Answers
# CHAPTER 3: Stacks & Queues
import copy

class Stack:
    def __init__(self, array):
        self.stack = array
        self.size = len(array)
        self.top = self.stack[len(self.stack)-1]
        self.topIndex = len(self.stack)-1
        self.minDict = {}
        self.min = None

    #add to the top
    def push(self, item):
        #loop through the Stack
        self.stack.append(item)
        self.top = item
        self.minDict[len(self.stack)-1] = self.min

    def pop(self):
        #remove the top
        if len(self.stack) == 0:
            return
        else:
            self.stack.pop(len(self.stack)-1)
            self.top = self.stack[len(self.stack)-1]
            self.topIndex = len(self.stack)-1

    def peek(self):
        #return top, don't remove
          #remove the top
        if len(self.stack) == 0:
            return None
        elif len(self.stack) == 1:
            return self.stack[0]
        else:
            return self.stack[len(self.stack)-1]

    def isEmpty(self):
        #return True iff empty
        if self.size == 0:
            return True
        else:
            return False

    def min(self):
        return self.minDict[self.top]

    def printStack(self):
        printList = []
        index = 0
        item = self.stack[index]
        while(item != self.top):
            printList.insert(0, item)
            index = index + 1
            item = self.stack[index]
        printList.insert(0, item)
        print(printList)

#---Questions

# Q1: Describe how you'd use a single array to implement three stacks

def question3_1(stack1, stack2, stack3):
    print("----------\n" + "3.1 Describe how you'd use a single array to implement three stacks\n" + "Input : ", end='')
    print("Each Stack object was made to record its current size as well as current top. With these indications, you could place \n these Stack objects within one array, as well as have a reference array to keep track of where each stack's Top starts at (and indicate this change with event handlers tracking changes with pop() and push())")

# ---------------

# Q2: Design a stack where there's a function min that returns the minimum element

def question3_2(stack1, stack2, stack3):
    print("----------\n" + "3.2  Design a stack where there's a function min that returns the minimum element\n")
    print("Seen within my Stack library, I've added a 'min' dictionary to keep track of what each element's min is when they are on top. As we pop and push, this is how we can track what the min is per stack top")


# Q3: How can you create a SetofStacks that holds multiple stacks, where a new stack is created once the last is overfilled?
def question3_3():
    print("----------\n" + "3.3 How can you create a SetofStacks that holds multiple stacks, where a new stack is created once the last is overfilled?\n")

class SetOfStacks():
    def __init__(self, array, capacity):
        self.stack = array
        self.top = array[len(array)-1]
        self.size = len(array)
        self.limit = capacity
        self.stackNumber = 0
        self.setDict = {}
        self.index = 0

    def push(self, item):
        #if limit has been reached, indicate new stack
        if self.limit == self.size:
            self.setDict[self.stackNumber] = self.index + 1 #record the current index
            self.stackNumber = self.stackNumber + 1 #increment stack number because of new stack
            self.limit = self.limit + self.limit
        self.stack.append(item)
        self.size = self.size + 1
        self.top = item
        self.index = self.index + 1

    def pop(self):
        #remove the top
        if self.size == 0:
            return
        elif self.size == 1:
            self.top = self.stack[self.size-1]
            self.topIndex = self.size-1
        else:
            self.top = self.stack[self.size-2]
            self.topIndex = self.size-2

    def popAt(self, stack_number):
        #example: pop at stack #3
        tempTop = self.setDict[stack_number]
        if self.size == 0:
            return
        elif self.size == 1:
            self.stack[tempTop] = self.stack[tempTop-1]
        else:
            self.stack[tempTop] = None

    def printStack(self):
        printList = []
        index = 0
        item = self.stack[index]
        while(item != self.top):
            printList.insert(0, item)
            index = index + 1
            item = self.stack[index]
        printList.insert(0, item)
        print(printList)


# Q4: Implement a MyQueue Class which implements a Queue using two stacks:
def question3_4():
    print("----------\n" + "3.4 Implement a MyQueue Class which implements a Queue using two stacks:\n")

class MyQueue:
    def __init__(self, push_stack: Stack):
        self.push_stack = push_stack
        self.pop_stack = Stack(push_stack.stack)

    def addQ(self, value: int):
        print('addQ')
        self.push_stack.push(value) # add the new value to the push_stack
        self.pop_stack.stack = self.push_stack.stack.copy()
        self.pop_stack.stack.reverse()

    def removeQ(self):
        print('pushStack')
        self.pop_stack.pop()
        # self.pop_stack.stack.reverse()
        self.push_stack.stack = self.pop_stack.stack.copy()

    def printQ(self):
        self.pop_stack.printStack()


# Q5: Write a program to sort stack such that the smallest items are on top. Use an additional temporary stack, do not copy elements into other data structures (such as array)
# Stack supports push, pop, peek and isEmpty
def question3_5():
    print("----------\n" + "3.5 Write a program to sort stack such that the smallest items are on top. Use an additional temporary stack, do not copy elements into other data structures (such as array) Stack supports push, pop, peek and isEmpty\n" + "Input : ", end='')

# Q6: Animal Shelter holds only dogs & cats, operates in 'first in, first out'. People must adopt oldest (based on time of arrival) of dogs, or can select if they want dog or cat (and get oldest animal of that type). Cannot select which specific animal they want. Create a data structure that maintains this system. Implement Enquque, deququeAny, dequeueDog, dequeueCat. You can use a LinkedList structure.
def question3_6():
    print("----------\n" + "3.6 Animal Shelter holds only dogs & cats, operates in 'first in, first out'. People must adopt oldest (based on time of arrival) of dogs, or can select if they want dog or cat (and get oldest animal of that type). Cannot select which specific animal they want. Create a data structure that maintains this system. Implement Enquque, deququeAny, dequeueDog, dequeueCat. You can use a LinkedList structure.\n")



#----------------------


def main():
    print("LinkedList Python Library + Solutions to Chapter 2: LinkedLists")
    print("Written by Kamile Demir")
    stack = Stack([1,2,3,4])
    stack.push(9)
    print(stack.stack)
    print(stack.peek())
    stack.pop()
    stack.printStack()

    question3_3()
    SetofStacks = SetOfStacks([1,2], 3)
    print("Created SetOfStacks Class with push(), pop(), and popAt()")
    print("Initialized Set of Stacks with capacity 3:")
    SetofStacks.printStack()
    print("Pushing 3rd element, causing second stack to form:")
    SetofStacks.push(3)
    SetofStacks.printStack()
    print("Pushing another element into second stack:")
    SetofStacks.push(4)
    SetofStacks.printStack()
    print("Popping from the FIRST stack:")
    SetofStacks.popAt(0)
    SetofStacks.printStack()

    question3_4()
    pushStack = Stack([1,2,3,5])
    print("Initializing queue")
    queue = MyQueue(pushStack)
    queue.printQ()
    print("Enqueue 8:", end='')
    queue.addQ(8)
    queue.printQ()
    print("Dequeue:", end='')
    queue.removeQ()
    queue.printQ()


main()
