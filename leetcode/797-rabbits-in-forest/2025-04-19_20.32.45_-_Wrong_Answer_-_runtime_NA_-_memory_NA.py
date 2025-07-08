class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        d = {}
        for num in answers:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        for key,value in d.items():
            if key == 0:
                res += value
            else:    
                res += key + 1

        
        return res
