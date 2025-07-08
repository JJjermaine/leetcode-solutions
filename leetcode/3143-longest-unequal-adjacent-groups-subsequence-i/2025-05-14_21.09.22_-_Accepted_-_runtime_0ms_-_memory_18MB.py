class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # get longest subsequence from groups
        res = [words[0]]
        curr = 0
        for i in range(1, len(words)):
            if groups[i] != groups[curr]:
                res.append(words[i])
                curr = i

        return res

        