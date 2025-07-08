class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i=0
        res=0
        sign = 1
        while i<n and s[i]==' ':
            i+=1
        if  i<n and s[i]=='+':
            sign =1
            i+=1
        elif  i<n and s[i]=='-':
            sign=-1
            i+=1
        
        while i <n and '0' <= s[i] <= '9':
            res = res * 10 + (ord(s[i]) - ord('0'))
            i=i+1
        
        res = max(min(res * sign, 2**31 - 1), -2**31)
        return res