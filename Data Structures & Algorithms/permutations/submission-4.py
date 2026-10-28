class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(start):
            if start == len(nums):
                res.append(nums.copy())
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]

                backtrack(start+1)

                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return res

# [1, 2, 3]
# choose one number
# choose another one
# and another one. Order does matter