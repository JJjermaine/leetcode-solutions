class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            temp_nums = nums[l[i]:r[i]+1]

            temp_nums.sort()
            if len(temp_nums) < 2:
                res.append(True)
            else:
                operation = abs(temp_nums[0] - temp_nums[1])

                added = False
                for i in range(1, len(temp_nums)):
                    if abs(temp_nums[i-1] - temp_nums[i]) != operation:
                        res.append(False)
                        added = True
                        break

                if not added:
                    res.append(True)

        return res