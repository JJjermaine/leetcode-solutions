class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        if all(tops[i] == bottoms[i] or tops[i] == tops[0] or bottoms[i] == bottoms[0] for i in range(n)):
            return 0 

        temp1, temp2 = tops[0], bottoms[0]
        res1, res2 = 0, 0
        for i in range(1, n):
            if tops[i] == temp1:
                continue            
            elif bottoms[i] != temp1:
                break
            res1 += 1

        for i in range(1, n):
            if bottoms[i] == temp2:
                continue            
            elif tops[i] != temp2:
                break
            res2 += 1
        if res1 == res2 == 0:
            return -1
        if res1 == 0:
            return res2
        return res1




        