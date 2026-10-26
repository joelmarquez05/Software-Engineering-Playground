class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = s.lower()
        left = 0
        right = len(s) - 1
        while (left < right):
            if (not clean_s[left].isalnum()):
                left += 1
            elif (not clean_s[right].isalnum()):
                right -= 1
            elif (clean_s[left] == clean_s[right]):
                left += 1
                right -= 1
            else:
                return False
        return True
        
