# CTCI Questions & Answers
# CHAPTER 3: Stacks & Queues

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
        self.stack[len(self.stack)-1] = item
        self.top = item
        self.minDict[len(self.stack)-1] = self.min

    def pop(self):
        #remove the top
        if len(self.stack) == 0:
            return
        elif len(self.stack) == 1:
            self.top = self.stack[len(self.stack)-1]
            self.topIndex = len(self.stack)-1
        else:
            self.top = self.stack[len(self.stack)-2]
            self.topIndex = len(self.stack)-2

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
    def __init__(self, array):
        self.stack = array
        self.setNumber = 0
        self.top = [] #the top of each array

    def push(self, Stack):
        self.setNumber = self.setNumber + 1
        self.stack = self.stack + Stack.stack
        # self.top[self.setNumber-1] = Stack.topIndex

    def pop(self, Stack):


# Q4: Implement a MyQueue Class which implements a Queue using two stacks:
def question3_4():
    print("----------\n" + "3.4 Implement a MyQueue Class which implements a Queue using two stacks:\n")

class QueueStack:
    def __init__(self, push_stack: Stack):
        self.push_stack = push_stack
        self.pop_stack = []

    def addQ(self, value: int):
        self.push_stack.push(value) # add the new value to the push_stack
        temp = copy.copy(self.push_stack.stack)
        temp = temp.reverse()
        self.pop_stack = temp   # this is for keeping the push_stack and pop_stack identical

    def removeQ(self):
        self.push_stack.pop()
        temp = copy.copy(self.push_stack.stack)
        temp = temp.reverse()
        self.pop_stack = temp   # this is for keeping the push_stack and pop_stack identical

    def printQ(self):
        self.push_stack.printStack()

# Q5: Write a program to sort stack such that the smallest items are on top. Use an additional temporary stack, do not copy elements into other data structures (such as array)
# Stack supports push, pop, peek and isEmpty
def question3_5():
    print("----------\n" + "3.5 Write a program to sort stack such that the smallest items are on top. Use an additional temporary stack, do not copy elements into other data structures (such as array) Stack supports push, pop, peek and isEmpty\n" + "Input : ", end='')

# Q6: Animal Shelter holds only dogs & cats, operates in 'first in, first out'. People must adopt oldest (based on time of arrival) of dogs, or can select if they want dog or cat (and get oldest animal of that type). Cannot select which specific animal they want. Create a data structure that maintains this system. Implement Enquque, deququeAny, dequeueDog, dequeueCat. You can use a LinkedList structure.
def question3_6():
    print("----------\n" + "3.6 Animal Shelter holds only dogs & cats, operates in 'first in, first out'. People must adopt oldest (based on time of arrival) of dogs, or can select if they want dog or cat (and get oldest animal of that type). Cannot select which specific animal they want. Create a data structure that maintains this system. Implement Enquque, deququeAny, dequeueDog, dequeueCat. You can use a LinkedList structure.\n")



#----------------------


def main():
    stack = Stack([1,2,3,4])
    stack.push(9)
    print(stack.stack)
    print(stack.peek())
    stack.pop()
    stack.printStack()


main()
