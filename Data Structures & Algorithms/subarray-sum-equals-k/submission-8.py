from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_subarrays = 0
        n = len(nums)
        prefix_sum = 0
        counts = defaultdict(int)
        counts[0] = 1

        # prefix_sum - previous_sum = k
        for number in nums:
            prefix_sum += number # 2 -> 1 -> 2 -> 4
            previous_sum = prefix_sum - k

            total_subarrays += counts[previous_sum]

            counts[prefix_sum] += 1
        return total_subarrays