class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        only add open ( if open < n
        only add close ) if close < open
        when open == close == n then we save the result
        '''
        res = []
        stack = []
        def dfs(openN,closeN):
            if openN == closeN == n:
                res.append(''.join(stack))
                return
            if openN < n:
                stack.append('(')#Add
                dfs(openN+1,closeN)#explore
                stack.pop()#undo
            if closeN <  openN:
                stack.append(')')#Add
                dfs(openN,closeN+1)#explore
                stack.pop()#undo
        dfs(0,0)
        return res


        