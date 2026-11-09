class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        total = 1
        zero_amount = 0
        last_zero_index = 0

        for number in nums:
            if number == 0:
                zero_amount += 1
                continue
            total *= number
        
        if zero_amount >= 2:
            return [0] * n
        
        for number in nums:
            if zero_amount == 1:
                if number != 0:
                    res.append(0)
                else:
                    res.append(total)
            else:
                res.append(total//number)

        return res

    # time complexity: O(n)
    # space complexity: O(1) w/o res, otherwise O(n)
                
