class Solution:
    def minOperations(self, s: str) -> int:
        
        # check 01's
        count1 = 0
        for i in range(1, len(s), 2):
            if s[i-1] != "0":
                count1 += 1
            if s[i] != "1":
                count1 += 1
        if len(s)%2 != 0 and s[-1] != "0": count1 += 1

        # check 10's
        count2 = 0
        for i in range(1, len(s), 2):
            if s[i-1] != "1":
                count2 += 1
            if s[i] != "0":
                count2 += 1
        if len(s)%2 != 0 and s[-1] != "1": count2 += 1

        return min(count1, count2)



        