class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0] * 26
        for character in s:
            character_index = ord(character) - ord("a")
            freq[character_index] += 1
        for character in t:
            character_index = ord(character) - ord("a")
            freq[character_index] -= 1
        return all(count == 0 for count in freq)

        # space complexity = O(1)
        # time complexity = O(m+n), m = chars(s), n = chars(t)

        
        