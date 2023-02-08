class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Linked List'''

    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        self.capacity = capacity
        self.head = None
        self.num_items = 0

    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == 0:
            return True
        else:
            return False

    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == self.capacity:
            return True
        else:
            return False

    def push(self, item):
        '''If stack is not full, pushes item on stack.
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full() == False:
            node = Node(item)
            self.num_items += 1
            node.next = self.head
            self.head = node
           # # if self.head:
           # #    node.next = self.head.next
           # else:
           #     self.head = node
           #     self.head.next = None
        # if self.is_full() == False:
        #     Node = node(item)
        #     if self.tail:
        #         self.tail.next = Node
        #         self.tail = Node
        #     else:
        #         self.head = Node
        #         self.tail = Node
        #         self.num_items += 1
        else:
            raise IndexError

    def pop(self):
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        self.num_items -= 1
        if self.is_empty() == False:
            pop = self.head.data
            self.head = self.head.next
            # self.items[self.num_items] == [None]
            return pop
        if self.is_empty() == True:
            raise IndexError

    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty() == True:
            raise IndexError
        else:
            return self.head.data

    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return self.num_items
