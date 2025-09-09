class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        bank = {}

        for i in nums:
            bank[i] = 1 + bank.get(i, 0)

        for key, val in bank.items():
            freq[val].append(key)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return 
