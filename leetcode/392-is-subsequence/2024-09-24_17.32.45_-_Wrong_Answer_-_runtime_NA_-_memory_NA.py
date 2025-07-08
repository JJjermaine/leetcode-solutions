class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): # edge case, s needs to be greater
            return False
        
        if s == "": # edge case, s is empty
            return True

        s_pointer = 0
        t_pointer = 0
        
        # while both pointers dont reach the end and 
        # while t pointer equals s pointer, execute accordingly
        while s_pointer < len(s)-1 and t_pointer < len(t)-1:
            while t[t_pointer] == s[s_pointer]:
                s_pointer += 1
                t_pointer += 1
            else:
                t_pointer += 1

        # if s_pointer reaches the end, that means it matches with everything in t
        return s_pointer + 1 == len(s)
            
        