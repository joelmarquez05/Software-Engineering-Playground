class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_length = 0
        for right in range(len(s)):
            c = s[right]
            if c in seen: # dvdf
                while s[left] != c:
                    seen.remove(s[left])
                    left += 1
                left += 1
            else:
                max_length = max(right - left + 1, max_length)
                seen.add(c)
        return max_length
