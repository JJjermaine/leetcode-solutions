class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic = {}
        
        for row in range(len(mat)):
            count = 0
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    count += 1
            dic[row] = count

        s = sorted(dic.items(), key=lambda x: x[1]) # sort by value

        res = []


        for i in range(len(s)):
            if i >= k: break
            res.append(s[i][0])
 

        return res

        
            

        