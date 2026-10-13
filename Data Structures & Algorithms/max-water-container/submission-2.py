class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        currArea = 0
        while l < r:
            currArea = min(heights[l], heights[r]) * (r - l)
            res = max(res, currArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res