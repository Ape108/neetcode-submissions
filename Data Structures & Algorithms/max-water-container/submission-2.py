class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        while l < r:
            newArea = min(heights[l], heights[r]) * (r - l)
            maxArea = max(maxArea, newArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea