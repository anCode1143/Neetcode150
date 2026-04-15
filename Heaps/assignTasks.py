import heapq
from typing import List

def assignTasks(servers: List[int], tasks: List[int]) -> List[int]:
    free = [(weight, index) for index, weight in enumerate(servers)]
    heapq.heapify(free)
    time = 0
    working = [] # (timeFree, weight, index)
    answer = []
    taskIndex = 0
    while taskIndex < len(tasks):
        if taskIndex > time:
            time = taskIndex
        while len(working) > 0 and working[0][0] <= time:
            _, weight, index = heapq.heappop(working)
            heapq.heappush(free, (weight, index))
        if free:
            server = heapq.heappop(free)
            heapq.heappush(working, (time+tasks[taskIndex], server[0], server[1]))
            answer.append(server[1])
            taskIndex += 1
        else:
            time = working[0][0] if working else time

    return answer

print(assignTasks([3,3,2], [1,2,3,2,1,2]))