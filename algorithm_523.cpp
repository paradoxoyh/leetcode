class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        vector<int> sum(nums.size(), 0);
        for(int loop = 0; loop < nums.size(); loop++)
        {
            sum[loop] = nums[loop];
            for(int i = loop - 1; i >=0; i--)
            {
                sum[i] = nums[i] + sum[i + 1];
                if(k == 0?sum[i] == 0:sum[i]%k == 0) return true;
            }
        }
        return false;
    }
};
