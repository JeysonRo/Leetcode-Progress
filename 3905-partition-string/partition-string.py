class Solution:
    def partitionString(self, s: str) -> List[str]:
        segments = dict()
        cur_segment = ""
        for i in s:
            cur_segment += i
            if cur_segment in segments:
                continue
            else:
                segments[cur_segment] = 0
                cur_segment = ""
        
        return list(segments.keys())