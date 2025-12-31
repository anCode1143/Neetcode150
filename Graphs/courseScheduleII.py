from typing import List
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    roadmap = []
    coursePrereqs = {prerequisite : [] for prerequisite in range(numCourses)}
    for prerequisite in prerequisites:
        coursePrereqs[prerequisite[0]].append(prerequisite[1])

    provenCourses = set()
    visiting = set()
    def canDo(course):
        if not coursePrereqs[course] and not course in provenCourses:
            provenCourses.add(course)
            roadmap.append(course)
            return True
        if course in provenCourses:
            return True
        if course in visiting:
            return False
        visiting.add(course)
        for prerequisite in coursePrereqs[course]:
            if not canDo(prerequisite):
                return False
        provenCourses.add(course)
        visiting.remove(course)
        roadmap.append(course)
        return True
    for course in range(numCourses):
        if not canDo(course):
            return []
    return roadmap

print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
    
"""
cue for diagnosing pattern - the fact that data is connected to each other with directions

how to implement the solution
    implement topological sort from previous part
        init adjacency list
        have visiting and visit set
        implement dfs called for every module
            if theres no prereq, return true, add to visit.
            if visiting, return false for cycle detection
            else iterate prereqs checking if theyre doable. remove modules from visiting (backtracking properties)
    make conditional more explicit, when returning true, append the module to the answer

struggled parts - backtracking property of topological sort's cycle detection (general recursion stuff)

complexity details
    speed - O(N + P) the amount of courses adding the prerequisites, 
        this is in linear time as all nodes are only visited once given the use of sets
    memory - O(N + P), stores the adjacency list and iterates through lists 
"""