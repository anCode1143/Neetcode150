import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.students = nums
        self.cutoff = k
        heapq.heapify(self.students)
        while len(self.students) > self.cutoff:
            heapq.heappop(self.students)
        

    def add(self, val: int) -> int:
        if len(self.students) < self.cutoff:
            heapq.heappush(self.students, val)
        elif val > self.students[0]:
            heapq.heappushpop(self.students, val)
        return self.students[0]