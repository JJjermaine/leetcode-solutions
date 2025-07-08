class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        # make sure left sliding window is non increasing
        # make sure right sliding window is non decreasing
        # we dont care about i's number
        n = len(nums)

        # [2, 3, 4, 5, 8, 12, 13] 
        # [True, True, True, False, False,-,  -]
        # compute all windows where k in non increasing
        nonInc = [False] * n
        violations = 0
        for i in range(k - 1):
            if nums[i] < nums[i+1]:
                violations += 1

        for l1 in range(n-k+1):
            l2 = l1 + k - 1
            if violations == 0:
                nonInc[l1] = True
            if l2 + 1 < n:
                if nums[l1] < nums[l1+1]:
                    violations -= 1
                if nums[l2] < nums[l2+1]:
                    violations += 1


        # [13, 11, 10, 9, 8, 5, 1]
        # [-, False, True, True, True, True, -]
        # compute all windows where k is non decreasing
        nonDec = [False] * n
        violations = 0
        for i in range(k - 1):
            if nums[i] > nums[i+1]:
                violations += 1

        for l1 in range(n-k+1):
            l2 = l1 + k - 1
            if violations == 0:
                nonDec[l1] = True
            if l2 + 1 < n:
                if nums[l1] > nums[l1+1]:
                    violations -= 1
                if nums[l2] > nums[l2+1]:
                    violations += 1
        res = []
        for i in range(k, n-k):
            if nonInc[i-1] and nonDec[i+1]:
                res.append(i)
        return res



        
        
