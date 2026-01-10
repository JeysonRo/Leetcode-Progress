class UnionFind:
    def __init__(self, n):
        self.parent = {v : v for v in n}
        self.rank = {v : 1 for v in n}
    
    def find(self, node): # return root parent 
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b): # True if successful, False if already in same set
        parenta = self.find(a)
        parentb = self.find(b)
        if parenta == parentb:
            return False
        if self.rank[parenta] > self.rank[parentb]:
            self.parent[parentb] = parenta
            self.rank[parenta] += self.rank[parentb]
        else:
            self.parent[parenta] = parentb
            self.rank[parentb] += self.rank[parenta]
            
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = set()
        for account in accounts:
            for i in range(1, len(account)):
                n.add(account[i])

        uf = UnionFind(n)

        for account in accounts:
            for i in range(1, len(account)):
                uf.union(account[1], account[i])

        account_name = {}
        
        unique_email_set = defaultdict(set)
        for account in accounts:
            for i in range(1, len(account)):
                account_name[uf.find(account[i])] = account[0]
                unique_email_set[uf.find(account[i])].add(account[i])
        
        for key in unique_email_set.keys():
            unique_email_set[key] = sorted(unique_email_set[key])
        
        res = []
        for key in unique_email_set.keys():
            name = account_name[key]
            res.append([name] + unique_email_set[key])
        
        return res