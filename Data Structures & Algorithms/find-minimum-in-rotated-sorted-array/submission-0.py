class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i, number in enumerate(nums):
            if (i == 0):
                minimum_value = number
            else:
                minimum_value = min(number, minimum_value)
        return minimum_value
        

        