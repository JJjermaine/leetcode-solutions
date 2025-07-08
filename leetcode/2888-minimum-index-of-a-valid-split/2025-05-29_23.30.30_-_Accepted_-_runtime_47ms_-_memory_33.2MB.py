class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        d = Counter(nums)
        # if most distinct element, greedily split and then check other side
        most_common_number, count = d.most_common(1)[0]
        n = len(nums)
        if count-1 <= len(nums)-count:
            return -1
        curr, other = 0, 0
        res = 0
        for i in range(n):
            if nums[i] == most_common_number:
                curr += 1
            else:
                other += 1
            if curr > other:
                res = i
                break
        curr, other = 0, 0
        for i in range(i, n):
            if nums[i] == most_common_number:
                curr += 1
            else:
                other += 1
        
        if curr < other:
            return -1
        return res


        