class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # sliding window, def not optimal
        n = len(code)
        if k == 0:
            return [0] * (n)
        
        if k > 0:
            l = 0
            r = k
            res = [sum(code[1:k+1])]
            curr_sum = sum(code[1:k+1])
            while len(res) != n:
                l += 1
                curr_sum -= code[l]
                if r == n-1:
                    r = 0
                    curr_sum += code[r]
                else:
                    r += 1
                    curr_sum += code[r]
                    
                res.append(curr_sum)
        if k < 0:
            l = len(code) + k
            r = len(code)-1

            res = [sum(code[k:])]
            curr_sum = sum(code[k:])
            while len(res) != n:
                if l == n-1:
                    curr_sum -= code[l]
                    l = 0
                else:
                    curr_sum -= code[l]
                    l += 1
                if r == n-1:
                    r = 0
                    curr_sum += code[r]
                else:
                    r += 1
                    curr_sum += code[r]
                    
                res.append(curr_sum)
        return res
