class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ""
        for i in range(2, len(num)):
            if num[i-2] == num[i-1] == num[i]:
                store = num[i-2] + num[i-1] + num[i]
                if largest == "":
                    largest = store
                if int(store) > int(largest) and largest != "":
                    largest = store

        return largest