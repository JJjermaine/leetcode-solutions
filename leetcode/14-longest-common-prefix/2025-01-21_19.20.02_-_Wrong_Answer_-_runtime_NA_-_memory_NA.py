class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # naive solution, get first letter and extend it and keep matching
        if "" in strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        strs.sort()
        longest = "" # string
        longest_i = 0
        i = 0
        while True:
            if longest != strs[i][:longest_i]:
                return strs[0][:longest_i-1]
            if i == len(strs) - 1: # reached the end of list, extend longest
                i = 0
                longest_i += 1
                longest = strs[0][:longest_i]
                if longest_i == len(strs[0]):
                    return longest
            i += 1
        return longest


        