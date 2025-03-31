class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zeros = 0
        length = len(flowerbed)

        if flowerbed == [0] and n == 1:
            return True

        for i in range(length):
            if n <= 0:
                return True
            else:
                if flowerbed[i] == 0:
                    zeros += 1
                else:
                    zeros = 0
            if zeros >= 3 or zeros >= 2 and i <= 1 or zeros >= 2 and i >= length - 1:
                zeros = 1
                n -= 1

        return n <= 0
