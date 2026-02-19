class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = defaultdict(set)
        answers = [-1 for i in range(len(queries))]

        for pre, course in prerequisites:
            adj[course].add(pre)

        @cache
        def dfs(course):
            res = set()
            res = res.union(adj[course])
            for pre in adj[course]:
                res = res.union(dfs(pre))
            adj[course] = set(res)
            return res
        
        for pre, course in queries:
            dfs(course)
        
        for i in range(len(queries)):
            pre = queries[i][0]
            course = queries[i][1]
            if pre in adj[course]:
                answers[i] = True
            else:
                answers[i] = False
            
        return answers