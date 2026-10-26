class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, number in enumerate(nums):
            if number == target:
                return i
        return -1
        