class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        cache = {}
        largest_square = 0

        def square_size(m,n):
            if (m,n) in cache:
                return cache[m,n]
            if m >= len(matrix) or n >= len(matrix[0]) or matrix[m][n] == "0":
                return 0
            else:
                cache[m,n] = min(square_size(m+1,n), square_size(m,n+1), square_size(m+1,n+1)) + 1
                return cache[m,n]
        
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                square = square_size(m,n)
                if largest_square < square:
                    largest_square = square
        
        return largest_square**2