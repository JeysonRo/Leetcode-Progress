class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        # monotonic increasing stack
        stack = [0]

        for i in range(1, len(nums)):
            if nums[i] > nums[stack[-1]]:
                stack.append(i)
        
        if stack[-1] != len(nums) - 1:
            stack.append(len(nums) - 1)
        
        score = 0

        for i in range(len(stack)-1):
            score += (stack[i+1] - stack[i]) * nums[stack[i]]
        
        return score