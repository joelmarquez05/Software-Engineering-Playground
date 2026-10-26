class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[mid] > nums[left]: # left sorted?
                    left = mid + 1
                else:
                    if nums[right] >= target:
                        left = mid + 1
                    else:
                        right = mid - 1
            else: # nums[mid] > target
                if nums[mid] < nums[right]: # right sorted?
                    right = mid - 1
                else:
                    if nums[left] <= target:
                        right = mid - 1
                    else:
                        left = mid + 1
        return -1

# nums=[3,4,5,6,1,2] # [3, 2] 
# target=1

# [3,4,5,6,1,2] target = 5
# [6,1,2,3,4,5] 
# mid < target 
# - we know right side is sorted 
#   - if right >= target => left = mid + 1
#   - if right < target => right = mid - 1
# - we know left side is sorted => left = mid + 1
# mid > target
# - we know right side is sorted => right = mid - 1
# - we know left side is sorted 
#   - if left < target => right = mid - 1
#   - if left > target => left = mid + 1

# [5,6,1,2,3,4]
# [5,6,1,2,3,4]