class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        suffix = 1
        # i = [0, n-1]
        # j = [n-1, 0]
        # j = n-1-i
        for i in range(n):
            j = n-1-i
            res[i] *= prefix
            res[j] *= suffix
            prefix *= nums[i]
            suffix *= nums[j]

        return res
    # time complexity:
    # space complexity:
                
