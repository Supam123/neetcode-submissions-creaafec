class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'}':"{",")":"(","]":"["}
        closing = [']','}',')']
        stack = []
        for bracket in s:
            if(bracket in closing):
                if(stack and stack[-1]==mapping[bracket]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return False if stack else True


        