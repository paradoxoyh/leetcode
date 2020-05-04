class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int i = 0;
        int res = 0;
        nums.push_back(nums.size() + 2);
        int invalidNum = nums.size() + 1;
        for(i = 0; i < nums.size(); i++)
        {
            while(true)
            {
                int temp = nums[i];
                if(temp == i || temp == invalidNum)
                {
                    if(temp == invalidNum)
                        res = i;
                    break;
                }
                nums[i] = nums[temp];
                nums[temp] = temp;
            }
        }
        return res;
    }
};
