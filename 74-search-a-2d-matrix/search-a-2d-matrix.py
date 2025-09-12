class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n

        while l < r:
            index = (r - l) // 2 + l
            matm = index // n
            matn = index % n
            num = matrix[matm][matn]
            if num == target:
                return True
            elif num > target:
                r = index
            else:
                l = index + 1
        return False