class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combination = []
        res = []

        # return unique combination nums sum = target
        # same number may be chosen repeatedly
        # num frequency criteria for similarity

        def backtrack(index, total_sum):
            if total_sum == target:
                res.append(combination.copy())
                return
            if total_sum > target:
                return
            
            for i in range(index, len(nums)):
                number = nums[i]
                combination.append(number)
                backtrack(i, total_sum+number)
                combination.pop()

        backtrack(0, 0)

        return res

            

