import string
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        sub_alphabet = ""
        pos = 0
        for c in key:
            if c == " ": continue
            if c not in sub_alphabet:
                sub_alphabet += c


        res = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for c in message:
            if c == " ": res += " "
            else:
                res += alphabet[sub_alphabet.index(c)]

        return res

