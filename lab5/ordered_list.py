class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of
list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        if self.head.next == self.head:
            return True
        else:
            return False

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''
        new_Node = Node(item)
        if self.is_empty() == True:
            self.head.next = new_Node
            self.head.prev = new_Node
            new_Node.prev = self.head
            new_Node.next = self.head
        else:
            current_Node = self.head.next
            prev_Node = self.head
            while current_Node != self.head:
                if new_Node.item > current_Node.item:
                    current_Node = current_Node.next
                    prev_Node = current_Node.prev
                elif new_Node.item < current_Node.item:
                    new_Node.next = current_Node
                    new_Node.prev = prev_Node
                    prev_Node.next = new_Node
                    current_Node.prev = new_Node
                    break
                else:
                    return False
            if current_Node == self.head:
                new_Node.next = self.head
                new_Node.prev = prev_Node
                prev_Node.next = new_Node
                self.head.prev = new_Node
        return True

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was
in the list)
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        remove_Node = self.head.next
        while remove_Node != self.head:
            if remove_Node.item == item:
                prev_Node = remove_Node.prev
                next_Node = remove_Node.next
                prev_Node.next = next_Node
                next_Node.prev = prev_Node
                return True
            else:
                remove_Node = remove_Node.next
        return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of
list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        index_Node = self.head.next
        index = 0
        while index_Node != self.head:
            if index_Node.item == item:
                return index
            else:
                index_Node = index_Node.next
                index += 1
        return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        data_list = []
        index_Node = self.head.next
        counter = 0
        while index_Node != self.head:
            data_list.append(index_Node.item)
            counter += 1
            index_Node = index_Node.next
        if index < 0 or index > counter:
            raise IndexError
        else:
            index_Node = self.head.next
            while index_Node != self.head:
                if index_Node.item == data_list[index]:
                    temp = index_Node.item
                    prev_Node = index_Node.prev
                    next_Node = index_Node.next
                    prev_Node.next = next_Node
                    next_Node.prev = prev_Node
                    return temp
                else:
                    index_Node = index_Node.next
        return False

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        def helper(item, current_node):
            if current_node == self.head:
                return False
            elif current_node.item == item:
                return True
            else:
                return helper(item, current_node.next)

        return helper(item, self.head.next)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        ordered_List = []
        node = self.head.next
        while node != self.head:
            ordered_List.append(node.item)
            node = node.next
        return ordered_List

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using
recursion

           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        reverse_List = []

        def helper(current_Node: Node):
            while current_Node != self.head:
                reverse_List.append(current_Node.item)  #why doesn't item appear auto.
                current_Node = current_Node.prev
            return reverse_List
        return helper(self.head.prev)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        def helper(current_Node: Node):
            size = 0
            while current_Node != self.head:
                size += 1
                current_Node = current_Node.prev
            return size
        return helper(self.head.prev)


# t_list = OrderedList()
# print(t_list.is_empty())
# t_list.add(1)
# print(t_list.is_empty())
# print(t_list.pop(0))
# print(t_list.is_empty())
# t_list = OrderedList()
# t_list.add(1)
# t_list.add(2)
# t_list.add(0)
# t_list.add(5)
# print(t_list.python_list())
# print(t_list.index(5))
# print(t_list.remove(7))
# print(t_list.python_list())
# print(t_list.python_list_reversed())
# print(t_list.pop(1))
# print(t_list.python_list())
# print(t_list.python_list_reversed())
# print(t_list.size())
# t_list.add(7)
# print(t_list.python_list())
# print(t_list.python_list_reversed())
# print(t_list.size())
# print(t_list.remove(0))
# print(t_list.python_list())
# print(t_list.python_list_reversed())
# print(t_list.size())