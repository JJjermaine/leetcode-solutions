class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # move all 1's  to the right and make all 00 to 10
        res = []
        ones = 0
        leading = 0
        i = 0
        # count leading 1's as an edge case
        while binary[i] == "1":
            leading += 1
            i += 1

        for i in range(leading):
            res.append("1")

        for num in binary:
            if num == "0":
                res.append("0")
            else:
                ones += 1
        
        for i in range(ones - leading):
            res.append("1")


        for i in range(len(binary)-1):
            if res[i] == "0" and res[i+1] == "0":
                res[i], res[i+1] = "1", "0"
        return "".join(res)
        
                

        