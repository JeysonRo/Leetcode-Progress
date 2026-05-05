class NumArray:

    def __init__(self, nums: List[int]):
        cur_sum = 0
        self.prefix_sum_array = [0 for i in nums]

        for i in range(len(nums)):
            cur_sum += nums[i]
            self.prefix_sum_array[i] = cur_sum
        

    def sumRange(self, left: int, right: int) -> int:
        right_val = self.prefix_sum_array[right]

        if left == 0:
            left_val = 0
        else:
            left_val = self.prefix_sum_array[left-1]
        
        return right_val - left_val
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)