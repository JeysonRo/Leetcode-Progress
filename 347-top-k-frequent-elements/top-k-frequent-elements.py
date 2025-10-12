class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {1:[]} # freq[frequency] = num
        track = {} # track[num] = freq

        for num in nums:
            if num in track:
                freq[track[num]].remove(num)
                track[num] += 1
                if track[num] in freq:
                    freq[track[num]].append(num)
                else:
                    freq[track[num]]= [num]
            else:
                track[num] = 1
                freq[track[num]].append(num)
        print(freq)
        count = 0
        res = []
        for numlist in range(len(freq), 0, -1):
            for i in freq[numlist]:
                count += 1
                res.append(i)
                if count == k:
                    return res