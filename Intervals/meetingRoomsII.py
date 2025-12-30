from typing import List
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        startPointer, endPointer = 0, 0
        start.sort()
        end.sort()
        currMeetings = 0
        maxMeetings = 0
        while startPointer < len(intervals):
            if start[startPointer] < end[endPointer]:
                startPointer += 1
                currMeetings += 1
                maxMeetings = max(maxMeetings, currMeetings)
            elif start[startPointer] == end[endPointer]:
                endPointer += 1
                startPointer += 1
            else:
                endPointer += 1
                currMeetings -= 1
        return max(maxMeetings, len(end) - endPointer)


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res