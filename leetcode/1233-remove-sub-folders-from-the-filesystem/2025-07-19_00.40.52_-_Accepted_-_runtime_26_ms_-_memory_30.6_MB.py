class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]
        for i in range(1, len(folder)):
            last = res[-1] + "/"

            if last != folder[i][:len(last)]:
                res.append(folder[i])
        return res