class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        routes = [set(i) for i in routes]
        stops = defaultdict(set)

        for bus, route in enumerate(routes):
            for stop in route:
                stops[stop].add(bus)

        queue = deque()
        queue.appendleft(source)
        res = -1
        visited_buses = set()
        visited_stops = set()
        while queue:
            res += 1
            for i in range(len(queue)):
                stop = queue.pop()
                if stop == target:
                    return res
                for bus in stops[stop]:
                    if bus not in visited_buses:
                        visited_buses.add(bus)
                        for j in routes[bus]:
                            if j not in visited_stops:
                                queue.appendleft(j)
                                visited_stops.add(j)
        return -1