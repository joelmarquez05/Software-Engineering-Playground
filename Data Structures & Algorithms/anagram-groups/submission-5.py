from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        # frequencies -> the words
        index_freq = defaultdict(list)
        for word in strs:
            index_freq[tuple(sorted(word))].append(word)
        for freq in index_freq:
            res.append(index_freq[freq])
        return res









                 
        
    
        