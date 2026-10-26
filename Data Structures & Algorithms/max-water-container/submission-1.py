class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            res = max(res, (right-left) * min(heights[left], heights[right]))
            if (heights[left] > heights[right]):
                right -= 1
            elif (heights[left] < heights[right]):
                left += 1
            else:
                left += 1
                right -= 1
        return res

        