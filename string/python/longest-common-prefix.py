class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        if len(strs) == 0:
            return ""
        while True:
            for x in strs:
                if i == len(x) or x[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1
        return ""