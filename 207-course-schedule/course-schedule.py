class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}
        courses_taken = set()

        for a, b in prerequisites:
            adj[a].append(b)
        
        def dfs(cur, chain) -> bool:
            nonlocal courses_taken
            if cur in chain:
                return False
            chain.add(cur)
            while adj[cur]:
                prereq = adj[cur].pop()
                res = dfs(prereq, chain)
                if not res:
                    return False
            courses_taken = courses_taken.union(chain)
            chain.remove(cur)
            return True

        for key in adj.keys():
            if key in courses_taken:
                continue
            res = dfs(key, set())
            if not res:
                return False
            if len(courses_taken) == numCourses:
                return True

        if len(courses_taken) == numCourses:
            return True
        return False
