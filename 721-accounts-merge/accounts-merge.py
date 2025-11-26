class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = defaultdict(set)

        for acc_details in accounts:
            group = set()
            group.add(acc_details[0])
            for i in range(1, len(acc_details)):
                group.add(acc_details[i])
                if acc_details[i] not in emails:
                    emails[acc_details[i]] = group
                else: # prev account has email - union
                    print("union: ", acc_details[i])
                    emails[acc_details[i]].update(group)
                    group = emails[acc_details[i]]
                    for j in group:
                        emails[j] = group
        res = set()
        for i in emails.values():
            if tuple(i) not in res:
                print(i,tuple(i))
                res.add(tuple(i))
        final = []
        for i in res:
            # find name
            for j, n in enumerate(i):
                if len(n) >= 4 and (n[-4] == "." or n[-3] == "."):
                    continue
                else:
                    name = n
                    index = j
                    break
            
            final.append([name])
            final[-1] += sorted(list(i)[:index] + list(i)[index+1:])
        
        return final