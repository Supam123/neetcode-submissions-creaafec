class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        while l < r :
            width = r - l
            if heights[l] <= heights[r]:
                h = heights[l]
                l += 1
            else:
                h = heights[r]
                r -= 1
            curr_area = width*h
            area =  max(curr_area,area)
        return area

        