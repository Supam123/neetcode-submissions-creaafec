class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': return []
        mappings = {
                "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        curr_str = []
        def dfs(i):
            if len(curr_str) == len(digits):
                res.append(''.join(curr_str))
                return
            
            for j in mappings[digits[i]]:
                #digits = 24
                curr_str.append(j) # add
                dfs(i+1) # explore

                curr_str.pop() # undo
        dfs(0)
        return res