class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(curr):
            res.append(curr)
            if curr * 10 <= n:
                dfs(curr*10) # handles 1 - 2
                
            if curr + 1 <= n and curr % 10 != 9:
                dfs(curr+1) # handles 10-20

        dfs(1)
        return res
                
                
            

        