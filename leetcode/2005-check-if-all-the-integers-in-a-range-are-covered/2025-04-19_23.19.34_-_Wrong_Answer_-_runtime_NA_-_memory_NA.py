class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = [0] * 51
        for l, r in ranges:
            for i in range(l, r+1):
                arr[i] = 1
        for i in range(left, right+1):
            if arr[i] == 1:
                return True
        
        return False
        