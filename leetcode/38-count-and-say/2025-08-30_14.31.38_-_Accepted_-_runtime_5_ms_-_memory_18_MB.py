class Solution:
    def countAndSay(self, n: int) -> str:
        temp = ""
        for i in range(n):
            if temp == "":
                res = "1"
            else:
                res = temp
                temp = ""


            count = 1
            number = res[0]
            for i in range(1, len(res)):
                if res[i] != number:
                    temp += str(count) + number
                    number = res[i]
                    count = 1
                else:
                    count += 1

            temp += str(count) + number
        return res

        