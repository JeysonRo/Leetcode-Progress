class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
        provinces = 0
        n = len(isConnected)

        def visitProvince(city):
            for i, val in enumerate(city):
                if i not in visited and val == 1:
                    visited.add(i)
                    visitProvince(isConnected[i])

        for i in range(n):
            if i not in visited:
                provinces += 1
                visitProvince(isConnected[i])
        
        print(visited)
        return provinces