class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = defaultdict(list)
        n = len(words)
        res = 0
        valid = False
        for i in range(n):
            if words[i] == words[i][::-1]:
                if not d[words[i]]:
                    d[words[i]] = [1]
                else:
                    d[words[i]][0] += 1
            elif words[i][::-1] in d:
                d[words[i][::-1]][1] += 1
            else:
                if not d[words[i]]: 
                    d[words[i]] += [1, 0]
                else:
                    d[words[i]][0] += 1

        addOdddouble = False
        for k, v in d.items():
            if len(v) == 1:# bbxxbb <- want double to be odd, 1, 3, 5... or even, 2, 4, 6...
                # even double case, add no matter what
                if len(v) % 2 == 0:
                    res += double * 2
                # odd double case
                else:
                    res += (v[0] - 1) * 2
                    addOdddouble = True
            else:
                orig, palindrome = v
                res += 4 * min(orig, palindrome)
        # add one of the OddDouble
        res += addOdddouble * 2
        return res