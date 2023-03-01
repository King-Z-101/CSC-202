import random
import time

class unorderedList:
    def __init__(self, size):
        self.size = size
        self.list = []

    def generateList(self):
        for i in range(self.size):
            self.list.append(i+1)
        random.shuffle(self.list)
        return self.list


def selection_sort(alist):
    comparisons = 0
    for i in range(1, len(alist)):
        min_position = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min_position]:
                min_position = j
            comparisons += 1
        alist[i], alist[min_position] = alist[min_position], alist[i]
    return comparisons


def insertion_sort(alist):
    comparisons1 = 0
    for i in range(1, len(alist)):
        current_value = alist[i]
        position = i
        while position > 0 and alist[position - 1] > current_value:
            comparisons1 += 1
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = current_value
    return comparisons1

alist = unorderedList(8000).generateList()
alist1 = unorderedList(8000).generateList()

#Record time and number of comparisons between insertion and selection
start1 = time.time()
insertion_comparisons = insertion_sort(alist)
end1 = time.time()
start2 = time.time()
selection_comparisons = selection_sort(alist1)
end2 = time.time()

print("Insertion Sort Comparisons:", insertion_comparisons)
print("Time:", (end1 - start1))
print()
print("Selection Sort Comparisons:", selection_comparisons)
print("Time:", (end2 - start2))

