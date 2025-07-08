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
            group_size = key + 1
            groups_needed = ceil(value / group_size)
            res += groups_needed * group_size

        
        return res
