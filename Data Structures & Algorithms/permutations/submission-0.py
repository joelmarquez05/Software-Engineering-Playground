class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []
        used_numbers = set()

        def backtrack(index):
            if index == len(nums):
                res.append(path.copy())
                return
            
            for number in nums:
                if number in used_numbers:
                    continue
                path.append(number)
                used_numbers.add(number)
                print(used_numbers)
                backtrack(index+1)
                used_numbers.remove(number)
                path.pop()
        
        backtrack(0)
        return res

# [1, 2, 3]
# choose one number
# choose another one
# and another one. Order does matter