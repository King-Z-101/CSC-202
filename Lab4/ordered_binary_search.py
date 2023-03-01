import random
import time


class orderedList:
    def __init__(self, size):
        self.size = size
        self.list = []

    def generateList(self):
        for i in range(self.size):
            self.list.append(i+1)
        random.shuffle(self.list)
        return self.list

def bubbleSort(alist):
    for element in range(len(alist) -1, 0, -1):
        for i in range(element):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
    return alist

def binarySearch(newList, item):
    found = str(item) + " Not Found"
    if len(newList) == 0:
        return found
    else:
        midpoint = len(newList) // 2
        if newList[midpoint] == item:
            found = str(item) + " Found In:"
            return found
        else:
            if item < newList[midpoint]:
                return binarySearch(newList[:midpoint], item)
            else:
                return binarySearch(newList[midpoint+1:], item)


def main():
    #Create an Unordered list that is then sorted through bubble sort
    b = orderedList(10000)
    newList = bubbleSort(b.generateList())

    # Record how long it takes to find an item
    start0 = time.time()
    print(binarySearch(newList, 555))
    end0 = time.time()
    print((end0 - start0) * 1000, " ms ")
    print("-----")
    start1 = time.time()
    print(binarySearch(newList, 1750))
    end1 = time.time()
    print((end1 - start1) * 1000, " ms")
    print("-----")
    start2 = time.time()
    print(binarySearch(newList, 4850))
    end2 = time.time()
    print((end2 - start2) * 1000, " ms")
    print("-----")
    start3 = time.time()
    print(binarySearch(newList, 9053))
    end3 = time.time()
    print((end3 - start3) * 1000, " ms")
    print("-----")
    start4 = time.time()
    print(binarySearch(newList, 8564))
    end4 = time.time()
    print((end4 - start4) * 1000, " ms")
    print("-----")
    start5 = time.time()
    print(binarySearch(newList, 57575))
    end5 = time.time()
    print((end5 - start5) * 1000, " ms")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("\nProgram completed in", round((end - start) * 1000), "ms")

# Run #1:
# 555 Found In:
# 0.0  ms
# -----
# 1750 Found In:
# 0.0  ms
# -----
# 4850 Found In:
# 0.0  ms
# -----
# 9053 Found In:
# 1.0104179382324219  ms
# -----
# 8564 Found In:
# 0.0  ms
# -----
# 57575 Not Found
# 0.0  ms
#
# Program completed in 3746 ms
#Run #2:
# 555 Found In:
# 0.0  ms
# -----
# 1750 Found In:
# 0.0  ms
# -----
# 4850 Found In:
# 0.0  ms
# -----
# 9053 Found In:
# 0.0  ms
# -----
# 8564 Found In:
# 0.0  ms
# -----
# 57575 Not Found
# 0.0  ms
#
# Program completed in 3881 ms