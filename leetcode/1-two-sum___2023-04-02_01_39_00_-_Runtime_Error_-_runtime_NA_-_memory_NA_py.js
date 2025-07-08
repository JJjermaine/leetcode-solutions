class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        curr = 0
        next = 1
        back = len(nums) - 1
        news = []
        for i in nums: # reduce runtime
            if i < target:
                news.append(i)

        a = []
        while a != 0:
            if news[curr] + news[next] == target:
                a.append(curr)
                a.append(next)
                break
            elif next == back: # if compared index reaches the end
                curr += 1
                next = curr + 1
            else:
                next += 1

        return a

            
                