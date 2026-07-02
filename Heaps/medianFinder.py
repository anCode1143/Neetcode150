from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.store = SortedList()

    def addNum(self, num: int) -> None:
        self.store.add(num)

    def findMedian(self) -> float:
        if len(self.store) % 2 == 0:
            right = len(self.store) // 2
            left = right - 1
            return (self.store[left] + self.store[right]) / 2
        else:
            return self.store[len(self.store) // 2]