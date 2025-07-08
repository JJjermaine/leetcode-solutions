class Solution:
    def reformatNumber(self, number: str) -> str:
        res = ""
        for i in range(len(number)):
            count = 0
            if number[i] == " " or number[i] == "-":
                continue
            else:
                res += number[i]

        final = ""
        count = 0
        i = 0
        while i < len(res):
            if (len(res) - i) == 4: # there are 4 digits left, group in blocks of 2
                while count < 2:
                    final += res[i]
                    i += 1
                    count += 1
                final += "-"
                count = 0
                while count < 2:
                    final += res[i]
                    i += 1
                    count += 1

            else: # else group by 3s. Or 2s if last 2
                if (len(res) - i) == 2:
                    while count < 2:
                        final += res[i]
                        i += 1
                        count += 1
                    break
                while count < 3:
                    final += res[i]
                    
                    i += 1
                    count += 1
                final += "-"
            count = 0

        if final[-1] == "-":
            final = final[:-1]
        return final