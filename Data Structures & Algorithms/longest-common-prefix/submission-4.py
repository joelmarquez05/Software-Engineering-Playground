class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        for i in range(1, len(strs)):
            word = strs[i]
            if not word:
                return ""
            last_index = min(len(word), len(common_prefix))
            common_prefix = common_prefix[:last_index]

            for j in range(last_index):
                if word[j] != common_prefix[j]:
                    common_prefix = common_prefix[:j]
                    break
        return common_prefix
