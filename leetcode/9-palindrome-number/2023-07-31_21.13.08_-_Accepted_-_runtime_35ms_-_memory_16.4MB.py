class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        front = 0
        back = len(string) - 1

        while front < back:
            if string[front] != string[back]:
                return False
            front += 1
            back -= 1
        return True