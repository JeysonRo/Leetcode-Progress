class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        prereqs = defaultdict(set)
        next_courses = defaultdict(list)

        for req, next_course in relations:
            prereqs[next_course].add(req)
            next_courses[req].append(next_course)

        cur_time = 0
        min_heap = []


        for i in range(1, n+1):
            if len(prereqs[i]) == 0:
                heapq.heappush(min_heap, (time[i - 1], i)) 


        while min_heap:
            cur_time, course = heapq.heappop(min_heap)
            for next_course in next_courses[course]:
                prereqs[next_course].remove(course)
                if len(prereqs[next_course]) == 0:
                    heapq.heappush(min_heap, (cur_time + time[next_course - 1], next_course))
            
        return cur_time