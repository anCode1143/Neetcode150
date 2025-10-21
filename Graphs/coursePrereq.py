def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    prereqMap = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        prereqMap[course].append(prereq)

    visited = set()
    canDo = set()
    def dfs(course):
        if course in visited:
            return False
        if not prereqMap[course]:
            return True
        if course in canDo:
            return True
        
        visited.add(course)
        for prereq in prereqMap[course]:
            if dfs(prereq) == False:
                return False
        visited.remove(course)
        canDo.add(course)
        return True
    
    for course, _ in prereqMap.items():
        if dfs(course) == False:
            return False
    return True
