class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = {}

        for fro, to, price in flights:
            if fro in adj:
                adj[fro].append((to, price))
            else:
                adj[fro] = [(to, price)]
        
        visited = dict()
        minh = []
        heapq.heappush(minh, (0, src, k))
        cost = 0

        while minh and dst not in visited:
            price, src, stops = heapq.heappop(minh)
            if src in visited and visited[src] > stops:
                continue
            cost = max(price, cost)
            visited[src] = stops
            if stops >= 0:
                if src in adj:
                    for dest, destprice in adj[src]:
                        heapq.heappush(minh, (destprice + price, dest, stops - 1))
        
        if dst not in visited:
            return -1
        return cost