class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        d = defaultdict(list)
        for i in range(n):
            anagram = tuple(sorted(strs[i]))
            d[anagram].append(i)

        res = []
        for key, values in d.items():
            temp = []
            for i in values:
                temp.append(strs[i])
            res.append(temp)
        return res
             