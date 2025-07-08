class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        n = len(dominoes)
        for i in range(n):
            for j in range(i+1, n):
                if dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1] or dominoes[i][1] == dominoes[j][0] and dominoes[i][0] == dominoes[j][1]:
                    res += 1
        return res
        