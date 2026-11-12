class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water_captured = 0
        left_max = 0
        right_max = 0
        left = 0
        right = n - 1

        while left <= right:
            if left_max <= right_max:
                water_captured += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
                left += 1
            else:
                water_captured += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1
        return water_captured

    # [0 2 0 3 1 0 1 3 2 1 ]

    # space complexity = O(1)
    # time complexity = O(n)