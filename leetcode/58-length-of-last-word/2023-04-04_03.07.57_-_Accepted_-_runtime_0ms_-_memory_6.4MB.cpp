class Solution {
public:
    int lengthOfLastWord(string s) {
        int secondspace = 0;
        int count = 0;
        for (int i = s.length()-1; i >= 0; i--) {
            if ((s[i] == ' ') && (count > 0)) {
                break;
            }
            if (s[i] != ' ')
                count++;
        }
        return count;
    }
};