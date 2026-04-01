class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = min(heights[l], heights[r]) * (r - l)
        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            newArea = min(heights[l], heights[r]) * (r - l)
            maxArea = max(maxArea, newArea)
            
        return maxArea