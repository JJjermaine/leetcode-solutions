class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """ # naive solution, O(k)
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1

        # from left to right, decrement dictionary and only add the partition if all characters seen is decremented to 0
        seen = set()
        count = 0
        res = []
        for i in range(len(s)):
            seen.add(s[i])
            dic[s[i]] -= 1
            count += 1
            # if all character counts in set are 0, add to output and reset
            canPartition = all(dic.get(c) == 0 for c in seen)
            if canPartition:
                res.append(count)
                seen = set()
                count = 0
        return res
        """
        last = {c: i for i, c in enumerate(s)}  # last occurrence of each char
        res = []
        start = end = 0

        for i, c in enumerate(s):
            end = max(end, last[c])  # extend the partition to the farthest last occurrence
            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res

        