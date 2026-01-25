from typing import List
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    answer = []
    answer.append(intervals[0])
    for index in range(1, len(intervals)):
        if answer[-1][1] >= intervals[index][0]:
            answer[-1][1] = max(intervals[index][1], answer[-1][1])
        else:
            answer.append(intervals[index])
    return answer