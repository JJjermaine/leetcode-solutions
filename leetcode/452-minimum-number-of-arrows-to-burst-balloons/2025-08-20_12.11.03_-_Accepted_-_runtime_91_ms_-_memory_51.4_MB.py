class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort and greedily take most overlapping points
        if len(points) == 1:
            return 1
        points.sort(key=lambda x: x[-1])
        curr = 0
        check = 1
        res= 0 
        while check < len(points):
            while points[curr][-1] >= points[check][0]:
                check += 1
                if check == len(points):
                    break
                    
            res += 1
            curr = check
            check += 1
            if check == len(points):
                res += 1
                break
        return res