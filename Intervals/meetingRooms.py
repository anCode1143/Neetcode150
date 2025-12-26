from typing import List
def canAttendMeetings(self, intervals: List[Interval]) -> bool:
    if not intervals:
        return True
    intervals.sort(key=lambda val: val.start)
    for index in range(len(intervals)-1):
        if intervals[index].end > intervals[index+1].start:
            return False
    return True