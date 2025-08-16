class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        step = len(s) // k
        s_dic = defaultdict(int)
        t_dic = defaultdict(int)
        for i in range(0, len(s), step):
            s_dic[s[i:i+step]] += 1
            t_dic[t[i:i+step]] += 1
        return t_dic == s_dic