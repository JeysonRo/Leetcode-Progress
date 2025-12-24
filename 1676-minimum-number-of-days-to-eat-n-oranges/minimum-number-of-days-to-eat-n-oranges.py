class Solution:
    def minDays(self, n: int) -> int:

        visited = set([n])
        queue = deque()
        queue.appendleft(n)
        days = 0
        while queue:
            days += 1
            for i in range(len(queue)):
                n = queue.pop()
                if n == 1:
                    return days
                if n % 3 == 0:
                    if n//3 not in visited:
                        queue.appendleft(n//3)
                        visited.add(n//3)
                if n % 2 == 0:
                    if n//2 not in visited:
                        queue.appendleft(n//2)
                        visited.add(n//2)
                if n-1 not in visited:
                    queue.appendleft(n-1)
                    visited.add(n-1)