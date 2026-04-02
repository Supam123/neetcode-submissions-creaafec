class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+','-','*','/']

        for i in tokens:
            if i not in operands:
                stack.append(int(i))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                if i == '+':
                    res = (val1) + (val2)
                elif i == '*':
                    res = (val1) * (val2)
                elif i == '-':
                    res = (val1) - (val2)
                else:
                    res = int((val1) / (val2))

                stack.append(res)
        return stack[-1]
            