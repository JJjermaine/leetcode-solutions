class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = defaultdict(int)
        res = 0
        for a, b in dominoes:
            if ((a,b) in d or (b,a) in d):
                res += d.get((a, b), d.get((b, a), None))

            d[(a,b)] += 1
            if a != b:
                d[(b,a)] += 1
        return res
        