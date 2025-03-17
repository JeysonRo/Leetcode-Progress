class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum = 0
        existing0 = False
        even = True
        lowest = abs(matrix[0][0])
        for row in matrix:
            for col in row:
                if col < 0:
                    even = (even == False) # weird way of creating a true false switch
                if col == 0:
                    existing0 = True
                lowest = min(lowest, abs(col))
                sum += abs(col)

        if existing0 or even:
            return sum
        else:
            return sum - 2 * lowest