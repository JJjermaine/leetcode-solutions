class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int elem_sum = 0;
        int dig_sum = 0;
        for (int i =0;i<nums.size();i++) {
            elem_sum += nums[i];
            while(nums[i]>0) {
                dig_sum += nums[i] % 10;
                nums[i] /= 10;
            }
        }
        return abs(elem_sum - dig_sum);
    }
};