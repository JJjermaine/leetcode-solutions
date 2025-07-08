class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for c in s1:
            if c not in s1_count:
                s1_count[c] = 1
            else:
                s1_count[c] += 1

        s1_window_length = sum(s1_count.values()) 

        s2_count = {}

        l = 0
        for r in range(len(s2)):
            if s2[r] not in s2_count:
                s2_count[s2[r]] = 1
            else:
                s2_count[s2[r]] += 1

            s2_window_length = sum(s2_count.values()) 
            
            if s1_window_length == s2_window_length:
                if s1_count == s2_count:
                    return True
                else:
                    s2_count[s2[l]] -= 1
                    if s2_count[s2[l]] == 0:
                        del s2_count[s2[l]]
                    l += 1
        
        return False