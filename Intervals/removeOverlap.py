from typing import List

def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort()
    prevEnd = intervals[0][1]
    answer = 0
    for interval in intervals[1:]:
        start, end = interval
        if prevEnd > start:
            answer += 1
            prevEnd = min(prevEnd, end)
        else:
            prevEnd = end
    return answer