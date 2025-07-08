class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set()
        for c in allowed:
            s.add(c)
        res = 0
        for word in words:
            add = True
            for c in word:
                if c not in s:
                    add = False
            if add: res += 1
        return res
                

                

        