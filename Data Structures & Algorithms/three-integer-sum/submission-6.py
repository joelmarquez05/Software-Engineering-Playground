class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        unique_triplets = set()

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                result = nums[i] + nums[left] + nums[right]

                if result > 0:
                    right -= 1

                elif result < 0:
                    left += 1

                else:
                    unique_triplets.add(
                        (nums[i], nums[left], nums[right])
                    )
                    left += 1
                    right -= 1

        return [list(element) for element in unique_triplets]