class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # put banned numbers in a set for O(1) look up
        banned_set = set()
        for num in banned:
            banned_set.add(num)
        
        curr = 0
        count = 0
        for i in range(1, n+1):
            if i in banned_set:
                continue
            curr += i
            count += 1
            if curr > maxSum:
                return count-1
        return count
       
        