class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                 height = min(heights[i], heights[j])
                 width = j-i
                 current = height * width
                 maximum = max(current, maximum)
        return maximum