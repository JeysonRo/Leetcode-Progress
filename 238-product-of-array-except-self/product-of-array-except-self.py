class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_product = []
        cur_product = 1
        for i in range(len(nums)):
            cur_product *= nums[i]
            left_product.append(cur_product)

        right_product = [1 for i in nums]
        cur_product = 1
        for i in range(len(nums)-1,-1,-1):
            cur_product *= nums[i]
            right_product[i] = cur_product
        
        res = []
        for i in range(len(nums)):
            if i-1 >= 0:
                left = left_product[i-1]
            else:
                left = 1
            if i+1 < len(nums):
                right = right_product[i+1]
            else:
                right = 1
            product = left * right
            res.append(product)
        
        return res