class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_valid_index = -1
        for i, number in enumerate(nums):
            if number != 0:
                last_valid_index = i
        
        if last_valid_index == -1:
            return
        
        i = 0
        while i < len(nums):
            if last_valid_index > i and nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                last_valid_index -= 1
            else:
                i += 1