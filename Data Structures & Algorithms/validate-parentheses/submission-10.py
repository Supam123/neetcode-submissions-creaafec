class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {')':'(',']':'[','}':'{'}
        stack = []
        closing =[")","}","]"]
        for bracket in s:
            if bracket in closing:
                if(stack and stack[-1]==mapping[bracket]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        if( len(stack) ==0):
            return True
        else:
            return False



        