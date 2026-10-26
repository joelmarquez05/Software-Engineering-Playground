class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_length = 0
        left = 0
        char_freq = [0] * 26

        for right in range(n):
            char_freq[ord(s[right]) - ord('A')] += 1

            while right - left + 1 - max(char_freq) > k:
                char_freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length