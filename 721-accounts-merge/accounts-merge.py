class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
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

        uf = UnionFind(len(accounts))
        email_to_account = defaultdict(int)

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    uf.union(email_to_account[email], i)
                else:
                    email_to_account[email] = i

        unique_accounts = defaultdict(list)
        for email, i in email_to_account.items():
            parent = uf.find(i)
            unique_accounts[parent].append(email)
        
        res = []
        for parent, emails in unique_accounts.items():
            account = email_to_account[emails[0]]
            name = accounts[account][0]
            res.append([name] + sorted(emails))
        
        return res