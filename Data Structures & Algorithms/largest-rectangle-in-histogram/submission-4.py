class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(0)
        for i,h in enumerate(heights):
            while stack and h <= heights[stack[-1]]:
                popped_index = stack.pop()
                height = heights[popped_index]
                right_boundary = i
                left_boundary = stack[-1] if stack else -1 
                
                width = right_boundary-left_boundary-1
                area = width*height
                max_area = max(area,max_area)
            stack.append(i)
        return max_area