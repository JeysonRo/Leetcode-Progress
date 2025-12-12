class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        
        for i, element in enumerate(nums):
            if target - element in hashmap:
                return [hashmap[target-element], i]
            else:
                hashmap[element] = i
        
        return [-1,-1]