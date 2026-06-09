class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maximum = 0
        while l < r:
            current = (min(heights[l], heights[r])) * (r - l)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            maximum = max(maximum, current)
        return maximum
    


