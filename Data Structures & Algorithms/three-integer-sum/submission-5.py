class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        unique_triplets = set()
        unique_values = set(nums)
        freq_value = {}

        for number in nums: # value -> freq
            freq_value[number] = freq_value.get(number, 0) + 1

        for i in range(n-1):
            for j in range(i+1, n):
                if -nums[i] - nums[j] in unique_values:
                    required_number = -nums[i]-nums[j]
                    
                    required_freq = 0

                    if (required_number == nums[i]):
                        required_freq += 1
                    
                    if (required_number == nums[j]):
                        required_freq += 1

                    if freq_value[required_number] <= required_freq:
                        continue

                    sorted_triplex = sorted((nums[i], nums[j], required_number))
                    unique_triplets.add(tuple(sorted_triplex))
        for element in unique_triplets:
            res.append(list(element))
        return res
        


# recover index from set
# value -> index

# nums: [-1, 0, 1, 2, -1, -4]

# set: [-4, -1, 0, 1, 2]
# need: [1 0 -1 -2 1 4]
# first pair needs -> 1



                    

