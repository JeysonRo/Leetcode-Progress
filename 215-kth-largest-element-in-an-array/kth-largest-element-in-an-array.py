class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)

        while k > 0:
            k -= 1
            res = heapq._heappop_max(nums)
        return res