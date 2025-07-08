class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        d = Counter(digits)
        temp = d.copy()
        for i in range(100, 999, 2):
            skip = False
            num = str(i)
            for c in num:
                c = int(c)
                if not d[c] or d[c] == 0:
                    skip = True
                    continue
                    
                d[c] -= 1
            d = temp.copy()
            if skip:
                continue
            res.append(i)

           
        return res
                