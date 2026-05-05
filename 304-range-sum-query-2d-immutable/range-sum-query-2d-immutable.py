class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.prefix_matrix = [[0 for col in range(COLS)] for row in range(ROWS)]
        
        for row in range(ROWS):
            for col in range(COLS):
                if col-1 < 0:
                    topsum = 0
                else:
                    topsum = self.prefix_matrix[row][col-1]
                if row-1 < 0:
                    leftsum = 0
                else:
                    leftsum = self.prefix_matrix[row-1][col]
                if col-1 >= 0 and row-1 >= 0:
                    diagsum = self.prefix_matrix[row-1][col-1]
                else:
                    diagsum = 0
                result = topsum + leftsum - diagsum
                self.prefix_matrix[row][col] = result + matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        bottom_left = self.prefix_matrix[row2][col1-1] if col1-1 >= 0 else 0
        top_right = self.prefix_matrix[row1-1][col2] if row1-1 >= 0 else 0
        diag = self.prefix_matrix[row1-1][col1-1] if row1-1 >= 0 and col1-1 >= 0 else 0
        res = diag-bottom_left-top_right
        res += self.prefix_matrix[row2][col2]
        
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)