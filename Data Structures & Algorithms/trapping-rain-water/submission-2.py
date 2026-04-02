class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxLwall = height[l]
        maxRwall = height[r]
        water = 0
        while l < r :
            if maxLwall < maxRwall:
                bottleneck = maxLwall
                l += 1
                water += max(0,bottleneck - height[l])
                maxLwall = max(maxLwall,height[l])
            else:
                bottleneck = maxRwall
                r -= 1
                water += max(0, bottleneck-height[r])
                maxRwall = max(maxRwall,height[r])
        return water

        