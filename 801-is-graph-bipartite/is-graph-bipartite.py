class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #bfs
        q = deque()

        setA = set()
        setB = set()
        isA = True
        i = 0
        while i < len(graph):
            while q:
                for i in range(len(q)):
                    node = q.pop()
                    for neighbor in graph[node]:
                        if neighbor not in setA and neighbor not in setB:
                            q.appendleft(neighbor)
                            if isA:
                                setB.add(neighbor)
                            else:
                                setA.add(neighbor)
                        if isA and neighbor in setA:
                            return False
                        elif not isA and neighbor in setB:
                            return False
                isA ^= True
            if i in setA or i in setB:
                i += 1
                continue
            else:
                q.appendleft(i)
                setA.add(i)
                isA = True
        
        return True