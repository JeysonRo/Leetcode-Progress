class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # recipes = list of recipes and their names
        # ingredients = list of recipes and the ingredients for each recipe
        # supplies = available ingredients

        adj_requires = {} # recipe : ingredients
        adj_possible_recipes = defaultdict(set)# ingredient : recipes containing ingredient

        for i, name in enumerate(recipes):
            adj_requires[name] = set(ingredients[i])
            for ingredient in ingredients[i]:
                adj_possible_recipes[ingredient].add(name)
        
        # bfs

        queue = deque()
        visited = set()
        res = set()
        for name in supplies:
            queue.appendleft(name)
            visited.add(name)

        while queue:
            name = queue.pop()
            for recipe in adj_possible_recipes[name]:
                if name in adj_requires[recipe]:
                    adj_requires[recipe].remove(name)
                if len(adj_requires[recipe]) == 0:
                    queue.appendleft(recipe)
                    if recipe not in visited:
                        visited.add(recipe)
                    if recipe not in res:
                        res.add(recipe)
        
        return list(res)