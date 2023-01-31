class Node: 
   def __init__(self,item):
       self.item = item
       self.next = None
   
class Queue:  
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''  
   
    def __init__(self, capacity):  
        '''Creates an empty Queue with a capacity'''  
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.num_items = 0
   
    def is_empty(self):  
        '''Returns True if the Queue is empty, and False otherwise  
           MUST have O(1) performance'''  
        if self.num_items == 0:
            return True
        else:
            return False
   
   
    def is_full(self):  
        '''Returns True if the Queue is full, and False otherwise  
           MUST have O(1) performance'''
        if self.num_items == self.capacity:
            return True
        else:
            return False
   
    def enqueue(self, item):  
        '''If Queue is not full, enqueues (adds) item to Queue   
           If Queue is full when enqueue is attempted, raises IndexError  
           MUST have O(1) performance'''  
        if self.is_full() == False:
            #Do sum big brain shit
            new_Node = Node(item)
            self.num_items += 1
            if self.tail:
                self.tail.next = new_Node
                self.tail = new_Node
            else:
                self.head = new_Node
                self.tail = new_Node
        else:
            raise IndexError
   
   
    # def dequeue(self):  
    #     '''If Queue is not empty, dequeues (removes) item from Queue and returns item.  
    #       If Queue is empty when dequeue is attempted, raises IndexError  
    #       MUST have O(1) performance'''  
    #     if self.is_empty() == False:
    #         # do sum stuff
    #     else:
    #         raise IndexError
    #     pass
   
   
    def size(self):  
        '''Returns the number of elements currently in the Queue, not the capacity  
           MUST have O(1) performance'''  
        return self.num_items 

q = Queue(5)  
print(q.is_empty())  
print(q.is_full())  
q.enqueue('thing') 
q.enqueue('that')
print(q.size())
print(q.is_empty())
print(q.head.item)
print(q.tail.item)
