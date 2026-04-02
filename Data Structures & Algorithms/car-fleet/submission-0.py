class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i],speed[i]))
        pairs.sort(reverse=True)

        stack = []
        for i in range(len(pairs)):
            time_to_target = ( target- pairs[i][0] ) / pairs[i][1]
            if stack and time_to_target > stack[-1]:
                stack.append(time_to_target)
            else:
                if not stack:
                    stack.append(time_to_target)
        return len(stack)
        


        