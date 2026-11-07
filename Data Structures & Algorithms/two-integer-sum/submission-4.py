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

# time complexity: O(n)
# space complexity: O(n)



                

