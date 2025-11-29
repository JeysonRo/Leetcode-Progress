class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        res = []
        def dfs(i, cur, section, sectionnum):
            if sectionnum > 3:
                return
            if i == len(s):
                if sectionnum == 3 and len(section) > 0 and len(section) < 4:
                    res.append(cur)
                return
            val = s[i]
            if len(section) == 0:
                dfs(i+1,cur + val, section + val, sectionnum)
            elif len(section) == 1:
                if section[0] != "0":
                    dfs(i+1, cur+val, section+val, sectionnum)
                dfs(i, cur+".", "", sectionnum+1)
            elif len(section) == 2:
                if section[0] in "1" or section[0] in "2" and (section[1] in "01234" or (section[1] == "5" and val in "012345")):
                    dfs(i+1, cur+val, section+val, sectionnum)
                dfs(i, cur+".", "", sectionnum+1)
            elif len(section) == 3:
                    dfs(i, cur+".", "", sectionnum+1)
        
        dfs(0, "", "", 0)
        return res