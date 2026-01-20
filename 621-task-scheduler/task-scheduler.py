class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = defaultdict(int)

        for task in tasks:
            task_dict[task] += 1
        
        maxheap = [] # minheap with negative insertion

        for task in task_dict.keys():
            heapq.heappush(maxheap, -task_dict[task]) # (freq, task)
        
        cooldown_q = deque()
        time = 0

        while maxheap or cooldown_q:
            time += 1
            if maxheap:
                task_count = heapq.heappop(maxheap)
                if task_count < -1:
                    cooldown_q.append((task_count+1, time + n)) # intervals left, time to finish cooldown
            while cooldown_q and cooldown_q[0][1] <= time:
                count, expire = cooldown_q.popleft()
                heapq.heappush(maxheap, count)
        return time            