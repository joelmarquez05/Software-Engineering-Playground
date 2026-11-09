from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        # frequencies -> words
        index_freq = defaultdict(list)
        for word in strs:
            word_frequencies = [0] * 26
            for character in word:
                word_frequencies[ord(character) - ord("a")] += 1
            index_freq[tuple(word_frequencies)].append(word)
        for freq in index_freq:
            res.append(index_freq[freq])
        return res

        # time complexity: O(n*m)
        # space complexity: O(n)









                 
        
    
        