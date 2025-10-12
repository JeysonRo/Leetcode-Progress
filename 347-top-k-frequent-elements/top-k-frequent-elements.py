class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {1:set()} # freq[frequency] = numset
        track = {} # track[num] = freq

        for num in nums:
            if num in track:
                track[num] += 1
            else:
                track[num] = 1
        
        for key in track.keys():
            if track[key] in freq:
                freq[track[key]].add(key)
            else:
                freq[track[key]] = set()
                freq[track[key]].add(key)

        count = 0
        res = []
        for num in range(len(nums), 0, -1):
            if num in freq:
                for i in freq[num]:
                    count += 1
                    res.append(i)
                    if count == k:
                        return res