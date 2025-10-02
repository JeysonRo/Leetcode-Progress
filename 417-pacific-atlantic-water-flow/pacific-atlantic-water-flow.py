class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        res = []
        visited = {} # visited[key][0] = True Pacific
                     # visited[key][1] = True Atlantic
        pacific = set()
        atlantic = set()
        # q = deque()
        # q.append((rows, 0))
        # q.append((0, cols))

        def dfsp(coord):
            r = coord[0]
            c = coord[1]
            if r < 0 or c < 0: # Pacific
                return
            if r >= rows or c >= cols: # Atlantic out of bounds
                return
            if coord in pacific:
                return
            pacific.add(coord)
            curheight = heights[r][c]
            
            if r > 0 and heights[r-1][c] >= curheight:
                dfsp((r-1,c))
            if r < rows-1 and heights[r+1][c] >= curheight:
                dfsp((r+1,c))
            if c > 0 and heights[r][c-1] >= curheight:
                dfsp((r,c-1))
            if c < cols-1 and heights[r][c+1] >= curheight:
                dfsp((r,c+1))
            
        
        def dfsa(coord):
            r = coord[0]
            c = coord[1]
            if r < 0 or c < 0: # Pacific
                return
            if r >= rows or c >= cols: # Atlantic out of bounds
                return
            if coord in atlantic:
                return
            atlantic.add(coord)
            curheight = heights[r][c]

            if r > 0 and heights[r-1][c] >= curheight:
                dfsa((r-1,c))
            if r < rows-1 and heights[r+1][c] >= curheight:
                dfsa((r+1,c))
            if c > 0 and heights[r][c-1] >= curheight:
                dfsa((r,c-1))
            if c < cols-1 and heights[r][c+1] >= curheight:
                dfsa((r,c+1))

        for i in range(rows):
            dfsp((i, 0))
            dfsa((i, cols-1))
        for i in range(cols):
            dfsp((0, i))
            dfsa((rows-1, i))

        for i in pacific:
            if i in atlantic:
                res.append([i[0], i[1]])

        return res