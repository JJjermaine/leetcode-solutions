class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        satisfied_prefix = [0] * (len(words) + 1)
        # calculate prefix sum array so query[i][1] - query[i][2] will be the range
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                satisfied_prefix[i + 1] = satisfied_prefix[i] + 1
            else:
                satisfied_prefix[i + 1] = satisfied_prefix[i]

        res = []
        for i in range(len(queries)):
            l, r = queries[i]
            curr = satisfied_prefix[r+1] - satisfied_prefix[l]
            res.append(curr)

        return res

        