class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_length = 0
        left = 0
        contained_zeros = 0

        for right in range(n):
            if nums[right] == 0:
                contained_zeros += 1
                while contained_zeros > k:
                    if nums[left] == 0:
                        contained_zeros -= 1
                    left += 1
            max_length = max(max_length, right - left + 1)
        
        return max_length

        # [1,1,1,0,0,0,1,1,1,1,0]
        # time complexity: O(n)
        # space complexity: O(1)