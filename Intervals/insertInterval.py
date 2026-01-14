def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    answer = []
    for index in range(len(intervals)):
        if newInterval[0] > intervals[index][1]:
            answer.append(intervals[index])
        elif newInterval[1] < intervals[index][0]:
            answer.append(newInterval)
            return answer + intervals[index:]
        else:
            newInterval = [min(newInterval[0], intervals[index][0]), max(newInterval[1], intervals[index][1])]
    answer.append(newInterval)
    return answer