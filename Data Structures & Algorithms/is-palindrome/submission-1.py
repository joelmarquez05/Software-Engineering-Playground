class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = []
        for char in s:
            if (char.isalnum()):
                clean_s.append(char.lower())
        final_s = "".join(clean_s)
        return final_s == final_s[::-1]
        
