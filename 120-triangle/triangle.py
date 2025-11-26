class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache = {}
        def dfs(layer, i):
            if (layer,i) in cache:
                return cache[layer,i]
            # we are on the last layer
            if layer == len(triangle) - 1:
                cache[layer,i] = triangle[layer][i]
                return triangle[layer][i]
            # continue to the next layer
            cache[layer,i] = min(dfs(layer+1, i), dfs(layer+1, i+1)) + triangle[layer][i]
            return cache[layer,i]
        
        return dfs(0,0)