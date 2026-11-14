class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        left = 0
        seen_characters = set()
        
        for right in range(n):
            while s[right] in seen_characters:
                seen_characters.remove(s[left])
                left += 1
            seen_characters.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length

# time complexity = O(n)
# space complexity = O(n)



        