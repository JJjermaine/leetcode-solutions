class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):  # Edge case: s is longer than t
            return False
        
        if s == "":  # Edge case: s is empty
            return True

        s_pointer = 0
        t_pointer = 0
        
        # Traverse both strings
        while s_pointer < len(s) and t_pointer < len(t):
            if t[t_pointer] == s[s_pointer]:  # If characters match, move s_pointer
                s_pointer += 1
            t_pointer += 1  # Always move t_pointer

        # If s_pointer reaches the end of s, it means all characters of s were found in t in sequence
        return s_pointer == len(s)
        