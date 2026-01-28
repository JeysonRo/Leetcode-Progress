class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()
        q.append((0, nums[0])) # (index, dp_val)
        res = nums[0]

        for i in range(1, n):
            if q and q[0][0] < i - k:
                q.popleft()

            cur = max(0 , q[0][1]) + nums[i]
            
            while q and cur > q[-1][1]:
                q.pop()
            
            q.append((i, cur))
            res = max(res, cur)
        
        return res