class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {}
        
        for num in range(numCourses):
            if num not in premap:
                premap[num] = []

        for crs, req in prerequisites:
            if crs in premap:
                premap[crs].append(req)

        visitSet = set()
        def dfs(course: int):
            if course in visitSet:
                return False
            if premap[course] == []:
                return True

            visitSet.add(course)
            for i in premap[course]:
                if not dfs(i):
                    return False
            visitSet.remove(course)
            premap[course] = []
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True