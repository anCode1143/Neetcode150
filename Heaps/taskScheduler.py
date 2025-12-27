from collections import deque
from typing import List
import heapq
def leastInterval(tasks: List[str], n: int) -> int:
    # count types of elements and add them to a max heap
    # loop while all heap and queue, keeping track of time, 
        # popping and decrementing, adding to queue, tracking when it can return to heap
    # return time
    taskAmount = {}
    for task in tasks:
        if task not in taskAmount:
            taskAmount[task] = 1
        else:
            taskAmount[task] += 1
    taskSchedule = []
    for _, taskCount in taskAmount.items():
        heapq.heappush(taskSchedule, -taskCount)
    idleTasks = deque()

    time = 0
    while idleTasks or taskSchedule:
        time += 1
        while idleTasks and idleTasks[0][1] <= time:
            currTask = idleTasks.popleft()
            heapq.heappush(taskSchedule, -currTask[0])
        if taskSchedule:
            currTask = -heapq.heappop(taskSchedule)
            currTask -= 1
            if currTask > 0:
                timeReady = time + n + 1
                idleTasks.append([currTask, timeReady])
    return time



class standardSolution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time