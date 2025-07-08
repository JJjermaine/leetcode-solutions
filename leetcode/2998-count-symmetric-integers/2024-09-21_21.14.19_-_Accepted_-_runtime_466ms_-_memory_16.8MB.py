class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        for i in range(low, high+1):
            string = str(i)

            if len(string) % 2 == 0: # odd nums are never symmetric, so perform algorithm if even
                n = len(string) // 2
                first_half = int(string[:n])
                second_half = int(string[n:])

                s1 = 0
                s2 = 0

                while first_half:
                    s1 += first_half % 10 # ex: 13, add 3
                    first_half //= 10 # 13 turns into 1

                while second_half:
                    s2 += second_half % 10
                    second_half //= 10 
                
                if s1 == s2:
                    count += 1

        return count

                

        