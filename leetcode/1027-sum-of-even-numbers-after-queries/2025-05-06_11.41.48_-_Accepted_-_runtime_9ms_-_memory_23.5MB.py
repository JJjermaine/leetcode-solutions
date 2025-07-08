class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # odd + odd -> even
        # even + even -> even
        # odd + even -> odd
        # even + odd -> odd
        # ^ same with minus

        curr = 0
        for num in nums:
            if num % 2 == 0:
                curr += num

        res = []
        for i in range(len(queries)):
            val, idx = queries[i]

            # whole index not added to curr
            if nums[idx] % 2 != 0: # odd
                nums[idx] += val
                if val % 2 != 0: # odd
                    curr += nums[idx]
                #else: # even
                    

            # val not added to curr
            elif nums[idx] % 2 == 0: # even
                nums[idx] += val
                if val % 2 == 0: # even
                    curr += val
                else: # odd
                    curr -= nums[idx] - val

            res.append(curr)
        return res

        