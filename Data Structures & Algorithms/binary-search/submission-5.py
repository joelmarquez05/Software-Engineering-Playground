class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle
            else:
                left = middle + 1

        if nums[left-1] == target:
            return left-1
        else:
            return -1
        

        