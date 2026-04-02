class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
   
        r = 0
        while r < len(temperatures):
            current_temp  = temperatures[r]

            while stack and current_temp > temperatures[stack[-1]]:
                popped_index = stack.pop()
                days_waited = r - popped_index
                res[popped_index] = days_waited
            stack.append(r)
            r += 1
        return res

        