class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = [0] * 26
        for character in s:
            character_index = ord(character) - ord("a")
            freq_s[character_index] += 1
        freq_t = [0] * 26
        for character in t:
            character_index = ord(character) - ord("a")
            freq_t[character_index] += 1
        return freq_s == freq_t
        
        