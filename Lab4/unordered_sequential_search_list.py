import random
import time

class randomList:
    def __init__(self, size):
        self.size = size
        self.randomList = []

    def generateList(self):
        for i in range(self.size):
            self.randomList.append(i+1)
        random.shuffle(self.randomList)
        return self.randomList


def sequentialSearch(list, item):
    pos = 0
    found = False
    start1 = time.time()
    if item > len(list):
        end1 = time.time()
        print(item, "not found:", (end1 - start1) * 1000, "ms")
    while pos < len(list) and not found:
        if list[pos] == item:
            found = True
            end = time.time()
            print(item, "found in", (end - start1) * 1000, "ms")
            break
        else:
            pos = pos + 1


def main():
    numList = randomList(10000)
    numList.generateList()
    sequentialSearch(numList.randomList, 555)
    sequentialSearch(numList.randomList, 1750)
    sequentialSearch(numList.randomList, 4850)
    sequentialSearch(numList.randomList, 9053)
    sequentialSearch(numList.randomList, 8564)
    sequentialSearch(numList.randomList, 57575)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("\nProgram completed in", round((end - start) * 1000), "ms")


# Run #1:
# 555 found in 0.0 ms
# 1750 found in 0.0 ms
# 4850 found in 0.5035400390625 ms
# 9053 found in 0.0 ms
# 8564 found in 1.0066032409667969 ms
# 57575 not found: 0.0 ms
#
# Program completed in 7 ms
# Run #2:
# 555 found in 0.0 ms
# 1750 found in 0.0 ms
# 4850 found in 1.0025501251220703 ms
# 9053 found in 0.0 ms
# 8564 found in 1.0001659393310547 ms
# 57575 not found: 0.5033016204833984 ms
#
# Program completed in 6 ms
#Run #3:
# 555 found in 0.0 ms
# 1750 found in 0.0 ms
# 4850 found in 0.0 ms
# 9053 found in 0.0 ms
# 8564 found in 1.0128021240234375 ms
# 57575 not found: 1.0001659393310547 ms
#
# Program completed in 6 ms


