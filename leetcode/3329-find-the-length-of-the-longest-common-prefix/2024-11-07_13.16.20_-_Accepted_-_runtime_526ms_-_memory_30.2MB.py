class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        store = set()
        set1 = set(arr1)

        for num in arr2:
            curr = ""
            for c in str(num):
                curr += c
                store.add(int(curr))

        res = 0
        for num in set1:
            curr = ""
            for c in str(num):
                curr += c
                if int(curr) in store:
                    res = max(res, int(len(curr)))
        return res

        