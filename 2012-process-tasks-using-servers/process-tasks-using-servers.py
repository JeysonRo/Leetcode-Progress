class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # servers = list of servers with their weight
        # tasks = list of tasks with their time needed to process (seconds)

        free = [] # (weight, index) of free servers
        busy = [] # (time, index) of busy servers
        time = 0
        cur_task = 0
        res = [0 for i in range(len(tasks))]

        for i in range(len(servers)):
            heapq.heappush(free, (servers[i], i))

        while cur_task < len(tasks):
            if cur_task > time:
                time += 1
                continue
            while busy and busy[0][0] <= time:
                freed_time, server_index = heapq.heappop(busy)
                heapq.heappush(free, (servers[server_index], server_index))
            if free:
                weight, server_index = heapq.heappop(free)
                heapq.heappush(busy, (time + tasks[cur_task], server_index))
                res[cur_task] = server_index
                cur_task += 1
            else:
                time = busy[0][0]

        return res