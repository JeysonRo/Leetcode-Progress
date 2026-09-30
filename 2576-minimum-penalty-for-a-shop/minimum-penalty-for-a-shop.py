class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix_open = [0 for c in customers]

        for i, character in enumerate(customers):
            if i == 0:
                prefix_val = 0
            else:    
                prefix_val = prefix_open[i-1]

            prefix_open[i] = prefix_val
            if character == "N":
                prefix_open[i] = prefix_val + 1

        min_penalty = prefix_open[i-1]
        day = len(customers)
        cur_penalty = 0
        
        for i in range(len(prefix_open)-1, -1, -1):
            if i == 0:
                prefix_val = 0
            else:
                prefix_val = prefix_open[i-1]
            if customers[i] == "Y":
                cur_penalty += 1
            if cur_penalty + prefix_val <= min_penalty:
                min_penalty = cur_penalty + prefix_val
                day = i

        return day