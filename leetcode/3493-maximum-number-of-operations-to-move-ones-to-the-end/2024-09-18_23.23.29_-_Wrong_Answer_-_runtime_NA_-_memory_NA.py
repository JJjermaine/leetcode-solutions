class Solution:
    def maxOperations(self, s: str) -> int:
        # edge case: ignore all the ones in the back
        ignored_ones = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "1":
                ignored_ones += 1
            else:
                break
        

        # edge case: double the count if back of array is zero
        double = False        
        if s[-1] == "0":
            double = True
            
        count = 0
        saved = 0    

        # edge case: check if first element a 1 to add to count
        if s[0] == "1":
            count += 1
            


        for i in range(1, len(s)):
            if s[i-1] == "0" and s[i] == "1":
                count += saved
                saved = count
                count += 1
            elif s[i] == "1":
                count += 1

        if double:
            return(count * 2)
        else:
            return(count - ignored_ones)