class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = 0
        result = []

        for kid in candies:
            greatest = max(greatest, kid)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)
        
        return result