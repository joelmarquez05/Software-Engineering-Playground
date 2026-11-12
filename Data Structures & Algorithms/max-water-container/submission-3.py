class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        left = 0
        right = n - 1

        while left < right:
            width = right - left
            if heights[left] < heights[right]:
                area = width * heights[left]
                max_area = max(area, max_area)
                left += 1
            else:
                area = width * heights[right]
                max_area = max(area, max_area)
                right -= 1
        return max_area

    # 1 7 2 5 4 7 3 6
    # time complexity = O(n)
    # space complexity = O(1)

        