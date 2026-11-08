class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        for i in range(1, len(strs)):
            word = strs[i]
            if not word:
                return ""
            last_index = min(len(word), len(common_prefix))
            
            j = 0

            while j < last_index:
                if word[j] != common_prefix[j]:
                    common_prefix = common_prefix[:j]
                    break
                j += 1
            common_prefix = common_prefix[:j]
        return common_prefix
