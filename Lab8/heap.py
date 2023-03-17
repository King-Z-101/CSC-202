class MaxHeap:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.size = 0
        self.heapList = [0]

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
     "item" can be any primitive or ***object*** that can be compared with other
     items using the < operator'''
        if self.is_full() == True:
            return False
        else:
            self.heapList.append(item)
            self.size += 1
            self.perc_up(self.size)
            return True
        # call percup which compares current item in array to parent and if greater they swap
    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty() == True:
            return None
        else:
            return self.heapList[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
     returns None if the heap is empty'''
        maxVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size -= 1
        self.heapList.pop()
        self.perc_down(1)
        return maxVal

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
     (This may be useful for in testing your implementation.)'''
        return self.heapList[1:]

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from
     the items in alist using the bottom-up construction method.
     If the capacity of the current heap is less than the number of
     items in alist, the capacity of the heap will be increased to accommodate the items in
    alist'''
        self.size = len(alist)
        if self.capacity < self.size:
            self.capacity = self.size
        i = len(alist) // 2
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.perc_down(i)
            i -= 1

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.size == 0

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.size >= self.capacity

    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.size

    def perc_down(self, i):
        '''where the parameter "i" is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        root = self.heapList[i]
        #check if root has left and right children
        if (i * 2 + 1) <= self.size:
            right_child = self.heapList[i * 2 + 1]
            left_child = self.heapList[i * 2]
            if root < left_child and root < right_child:
                if left_child > right_child:
                    temp = root
                    self.heapList[i] = left_child
                    self.heapList[i * 2] = temp
                    self.perc_down(i * 2)
                elif right_child > left_child:
                    temp1 = root
                    self.heapList[i] = right_child
                    self.heapList[i * 2 + 1] = temp1
                    self.perc_down(i * 2 + 1)
            elif root < left_child:
                temp = root
                self.heapList[i] = left_child
                self.heapList[i * 2] = temp
                self.perc_down(i*2)
            elif root < right_child:
                temp1 = root
                self.heapList[i] = right_child
                self.heapList[i * 2 + 1] = temp1
                self.perc_down(i * 2 + 1)
        #check if root only has left child
        elif (i * 2) <= self.size:
            left_child = self.heapList[i * 2]
            if root < left_child:
                temp = root
                self.heapList[i] = left_child
                self.heapList[i * 2] = temp
                self.perc_down(i * 2)

    def perc_up(self, i):
        '''where the parameter "i" is an index in the heap and perc_up moves the element stored
     at that location to its proper place in the heap rearranging elements as it goes.'''
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        index = len(alist) - 1
        size = len(alist)
        self.build_heap(alist)
        for i in range(size - 1):
                MaxValue = self.dequeue()
                alist[index] = MaxValue
                index -= 1
        return alist
