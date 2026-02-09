class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # dist = monsters and their distances (k) from our city
        # speed = monsters and their speeds (k/m)
        n = len(dist)
        arrival = [dist[i]/speed[i] for i in range(n)]
        arrival.sort()
        cur_time = 0
        res = 0
        for time in arrival:
            if cur_time >= time:
                return res
            res += 1
            cur_time += 1
        return res