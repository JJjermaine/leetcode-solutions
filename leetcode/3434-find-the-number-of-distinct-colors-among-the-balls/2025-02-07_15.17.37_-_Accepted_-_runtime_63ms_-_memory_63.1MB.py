class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        mp = {}
        color = defaultdict(int)
        ans = []
        
        for x, c in queries:
            if x in mp:
                old_color = mp[x]
                color[old_color] -= 1
                if color[old_color] == 0:
                    del color[old_color]
                    
            mp[x] = c
            color[c] += 1
            
            ans.append(len(color))
            
        return ans


        