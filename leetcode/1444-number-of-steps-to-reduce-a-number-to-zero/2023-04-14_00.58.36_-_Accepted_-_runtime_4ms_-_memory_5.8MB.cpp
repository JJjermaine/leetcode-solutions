class Solution {
public:
    int numberOfSteps(int num) {
        int count = 0;
        while (num > 0) {
            if (num % 2 == 0) {
                num /= 2;
                count += 1;
            }
            else {
                num -= 1;
                count += 1;
            }
        }
        return count;
    }
};