class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # tasks = list of tasks [(the time for this task to be added), processing time]
    
        for i in range(len(tasks)): # sort tasks by entask_queue time while preserving original index
            tasks[i].append(i)
        tasks.sort(key=lambda x : x[0])

        time = 0
        task_queue = [] # minheap (process_time, index)
        CPU = 0 # time that CPU will be available
        i = 0
        res = []

        while i < (len(tasks)):
            if CPU != 0:
                time += CPU
                CPU = 0
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(task_queue, (tasks[i][1], tasks[i][2]))
                i += 1
            if not task_queue:
                time = tasks[i][0]
                continue
            # pop from task queue
            process_time, index = heapq.heappop(task_queue)
                    
            res.append(index)
            CPU += process_time

        while task_queue:
            process_time, index = heapq.heappop(task_queue)
            res.append(index)
        
        return res