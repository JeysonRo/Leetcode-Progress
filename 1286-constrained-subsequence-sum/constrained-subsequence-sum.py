class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res = nums[0]
        max_heap = []
        heapq.heappush(max_heap, (-nums[0], 0))

        for i in range(1, len(nums)):
            while i - max_heap[0][1] > k:
                heapq.heappop(max_heap)

            cur_dp = max(nums[i], nums[i] - max_heap[0][0])
            res = max(res, cur_dp)
            heapq.heappush(max_heap, (-cur_dp, i))
        return res