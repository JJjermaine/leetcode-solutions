class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k = str(k)
        num.insert(0,0)
        j = len(num)-1
        for i in range(len(k)-1,-1,-1):
            num[j] += int(k[i])
            j -= 1

        for i in range(len(num)-1,-1,-1):
            if num[i] > 9:
                num[i-1] += num[i] // 10
                num[i] %= 10
            
        if num[0] == 0:
            num.pop(0)
        return num
        