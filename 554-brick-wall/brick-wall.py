class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # wall[row] = list of bricks and their width's
        ROWS = len(wall)
        COLS = sum(wall[0])

        edge_matrix = defaultdict(int)
        for r in range(len(wall)):
            edge = 0
            for i in range(len(wall[r])-1):
                brick = wall[r][i]
                edge += brick
                edge_matrix[edge] += 1
        res = 0
        for val in edge_matrix.values():
            res = max(res, val)
        return ROWS - res