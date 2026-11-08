class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs[0]:
            return ""
        last_common_index = len(strs[0])
        for i in range(1, len(strs)):
            word = strs[i]
            if not word:
                return ""
            last_index = min(len(word), last_common_index)
            
            j = 0

            while j < last_index:
                if word[j] != strs[0][j]:
                    break
                j += 1
            last_common_index = j
        return strs[0][:last_common_index]
