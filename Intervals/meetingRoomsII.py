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
    
"""
cue for diagnosing pattern - interval input

how to implement the solution
    create two sorted arrays of endings and beginings
    iterate pointer between min of next meetingend or meetingbegin. 
        if meeting end, current meetings reduced, else current meetings increase
        simulating time without running individual time
    return max recorded currmeetings

struggled parts - the solution, parsing the intervals into arrays

complexity details
    speed - nlogn for sorting, then there is linear time going through the two arrays
    memory - linear, stores arrays in proportion to the intervals given
"""