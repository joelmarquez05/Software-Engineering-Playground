from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        required_to_index = defaultdict(int)
        for i, number in enumerate(nums):
            required_to_index[target - number] = i
        for i, number in enumerate(nums):
            if number in required_to_index and i != required_to_index[number]:
                return [i, required_to_index[number]]
        return []

            
        
# [1, 3, 4, 2]
# target = 6

# 5: 0
# 3: 1
# 2: 2
# 4: 3
            
# [3, 4, 5, 6]
# [4, 3, 2, 1]
# [4, 5, 6]
# [6, 5, 4]
# required -> index
# 6 -> []
# 3 




                

