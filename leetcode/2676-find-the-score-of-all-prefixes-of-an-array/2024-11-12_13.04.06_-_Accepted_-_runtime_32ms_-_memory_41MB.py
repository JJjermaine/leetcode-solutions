class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        res = []
        count = 0
        max_num = 0
        for num in nums:
            max_num = max(max_num, num)
            if max_num > num:
                count += max_num + num
            else:
                count += num * 2
            res.append(count)
        return res