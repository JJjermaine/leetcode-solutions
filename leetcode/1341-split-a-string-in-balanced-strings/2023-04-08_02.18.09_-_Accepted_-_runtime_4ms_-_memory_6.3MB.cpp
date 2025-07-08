class Solution {
public:
    int balancedStringSplit(string s) {
        int count = 0;
        int bal = 0;
        for (char c : s) {
            if (c == 'R')
                bal--;
            else {
                bal++;
            }
            if (bal == 0) {
                count++;
            }
        }
        return count;
    }
};