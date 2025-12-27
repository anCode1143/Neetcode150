from typing import List
def canAttendMeetings(self, intervals: List[Interval]) -> bool:
    if not intervals:
        return True
    intervals.sort(key=lambda val: val.start)
    for index in range(len(intervals)-1):
        if intervals[index].end > intervals[index+1].start:
            return False
    return True

"""
cue for diagnosing pattern - interval values

how to implement the solution
    sort by first element
    compare a[1] with b[0]

struggled parts - lambda keyword, sorting with conditions

complexity details
    speed - n*log(n) due to sorting plus n for iteration
    space - O(1) in place sorting and variables

"""