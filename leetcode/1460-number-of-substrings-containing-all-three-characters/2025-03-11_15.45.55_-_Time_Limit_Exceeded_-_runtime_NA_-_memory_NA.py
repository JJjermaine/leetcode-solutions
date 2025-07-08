class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #sliding window to count all substrings that countain a b and c
        n = len(s)

        #table = {}
        count = 0

        for i in range(n):
            table = {}
            for j in range(i, n):
                if s[j] not in table:
                    table[s[j]] = 1
                else:
                    table[s[j]] += 1
            
                if "a" in table and "b" in table and "c" in table:
                    count += n - j
                    break
        return count

                
            

            


        