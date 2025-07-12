class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        # observations:
        # has to be squre shape so not greedy
        # see if bars can be removed by continuous bars, vertical AND horizontal 0: 1 -> 1: 4 -> 2: 9 -> 3: 16
        # can only remove [1, n-1] bars for both horizontal and vertical
        # max area at the start is 1, removing no bars

        if len(hBars) == 0 or len(vBars) == 0:
            return 1
        hBars.sort()
        vBars.sort()


        # keep track of longest continous
        hLongest = 1
        curr = 1
        prev = float("inf")
        for i in range(len(hBars)):
            if hBars[i] != 1 or hBars[i] != n+2:
                if hBars[i] == prev+1:
                    curr += 1
                else:
                    curr = 1
                hLongest = max(hLongest, curr)
            prev = hBars[i]

        # keep track of longest continuous
        vLongest = 1
        curr = 1
        prev = float("inf")
        for i in range(len(vBars)):
            if vBars[i] != 1 or vBars[i] != n+2:
                if vBars[i] == prev+1:
                    curr += 1
                else:
                    curr = 1
                vLongest = max(vLongest, curr)
            prev = vBars[i]
        
        takeAway = min(vLongest, hLongest)
        return (takeAway+1) ** 2  


            