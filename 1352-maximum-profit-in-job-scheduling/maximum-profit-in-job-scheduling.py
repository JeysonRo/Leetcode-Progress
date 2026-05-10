class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if len(profit) == 0:
            return 0
        
        queue = [] # (time, profit)

        jobs = [[startTime[i], endTime[i], profit[i]] for i in range(len(profit))]
        jobs.sort(key=lambda x : (x[0], x[1], x[2]))

        i = 0
        cur_profit = 0
        while i < len(jobs):
            cur_time = jobs[i][0]
            while queue and cur_time >= queue[0][0]:
                job_end, job_profit = heapq.heappop(queue)
                cur_profit = max(cur_profit, job_profit)

            heapq.heappush(queue, (jobs[i][1], cur_profit + jobs[i][2]))
            i += 1
        
        while queue:
            job_end, job_profit = heapq.heappop(queue)
            cur_profit = max(cur_profit, job_profit)
        
        return cur_profit