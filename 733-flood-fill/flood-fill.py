class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if color == original_color:
            return image
        def dfs(m,n):
            if m < 0 or m >= len(image) or n < 0 or n >= len(image[0]):
                return
            if image[m][n] == original_color:
                image[m][n] = color
                dfs(m+1,n)
                dfs(m-1,n)
                dfs(m,n+1)
                dfs(m,n-1)
            else:
                return
        
        dfs(sr, sc)
        return image