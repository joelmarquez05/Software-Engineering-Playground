class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def compute_subset(index, path):
            if index == len(nums):
                result.append(path.copy())
                return
            
            path.append(nums[index])
            compute_subset(index+1, path)
            path.pop()
            compute_subset(index+1, path)
        
        compute_subset(0, [])

        return result
            


        