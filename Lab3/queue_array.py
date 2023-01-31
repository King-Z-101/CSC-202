Class Queue: 
'''Implements an array-based, efficient first-in first-out Abstract Data Type   
       using a Python array (faked using a List)'''  
   
    def __init__(self, capacity):  
        '''Creates an empty Queue with a capacity'''  
        pass  
   
   
    def is_empty(self):  
        '''Returns True if the Queue is empty, and False otherwise  
           MUST have O(1) performance'''  
        pass  
   
   
    def is_full(self):  
        '''Returns True if the Queue is full, and False otherwise 
           MUST have O(1) performance'''  
        pass  
   
   
    def enqueue(self, item):  
        '''If Queue is not full, enqueues (adds) item to Queue   
           If Queue is full when enqueue is attempted, raises IndexError  
           MUST have O(1) performance'''  
        pass  
   
   
    def dequeue(self):  
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.  
           If Queue is empty when dequeue is attempted, raises IndexError  
           MUST have O(1) performance'''  
        pass  
   
   
    def size(self):  
        '''Returns the number of elements currently in the Queue, not the capacity  
           MUST have O(1) performance'''  
        pass 
