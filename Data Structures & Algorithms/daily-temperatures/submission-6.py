class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            curr = temperatures[i]

            while stack and curr > temperatures[stack[-1]]:
                popped_idx = stack.pop()
                res[popped_idx] = i - popped_idx
            stack.append(i)
        return res

        