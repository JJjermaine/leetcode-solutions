class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        res = ""
        l = 0
        s_count = {}
        have, need = 0, len(t_count)

        for r in range(len(s)):
            # Add the current character to s_count if it's in t_count
            if s[r] in t_count:
                s_count[s[r]] = s_count.get(s[r], 0) + 1
                # Check if this character has reached the required count
                if s_count[s[r]] == t_count[s[r]]:
                    have += 1

            # Once we have all the required characters in the current window
            while have == need:
                # Update result if the current window is smaller
                if res == "" or (r - l + 1) < len(res):
                    res = s[l:r + 1]

                # Move the left pointer to shrink the window
                if s[l] in t_count:
                    s_count[s[l]] -= 1
                    if s_count[s[l]] < t_count[s[l]]:
                        have -= 1
                l += 1

        return res if res != "" else ""
        