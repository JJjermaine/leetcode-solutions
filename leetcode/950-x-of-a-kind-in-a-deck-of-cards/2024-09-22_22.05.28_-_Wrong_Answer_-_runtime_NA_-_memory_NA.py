class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = {}
        for num in deck:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        
        min_division = min(d.values())
        if min_division == 1:
            return False

        for key, value in d.items():
            while value:
                value -= min_division
                if value < 0:
                    return False

        return True

        